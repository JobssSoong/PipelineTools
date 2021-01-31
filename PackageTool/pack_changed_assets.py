# coding=utf-8

import os, shutil
import json
import zipfile

ASSETS_PATTERN = 'E:/Project/Assets/{segment}/{name}/{version}/'

PREVIEW_PATTERN = 'E:/Project/Preview/{segment}/{name}/{version}/'

ASSETS_VERSION_PATTERN = 'E:/Project/'

VERSION_ARRAY = ['layout_model', 'correct_model', 'high_model', 'tex']

TEMP_DIR_PATTER = 'E:/Project/Temp/'



def get_asset_info(segment, version, name):
    path = ASSETS_PATTERN.format(segment=segment, name=name, version=version)
    p_path = PREVIEW_PATTERN.format(segment=segment, name=name, version=version)
    if not os.path.exists(path) and not os.path.exists(p_path):
        return []

    assets_info = []
    assets_info.append(path+os.listdir(path)[-1])
    p_lst = os.listdir(p_path)
    for i in p_lst:
        if i.endswith('json'):
            p_lst.remove(i)
    assets_info.append(p_path+p_lst[-1])

    return assets_info


def copy_to_temp_dir(file):
    temp_path = TEMP_DIR_PATTER + file[3:]
    if not os.path.exists(os.path.dirname(temp_path)):
        os.makedirs(os.path.dirname(temp_path))
    shutil.copy(file, temp_path)


def split_new_added_assets():
    new_version_info = dict()
    if os.path.exists(os.path.dirname(ASSETS_VERSION_PATTERN)+'/assets_version.json'):
        jsonname = os.path.dirname(ASSETS_VERSION_PATTERN)+'/assets_version.json'
        with open(jsonname) as file:
            version_info = json.load(file)

        #- Check Latest File
        for segment in version_info:
            new_version_info[segment] = dict()
            #- new_assets_lst：记录新添加的资产
            new_assets_lst = os.listdir(ASSETS_PATTERN.format(segment=segment, name='*', version='').split('*')[0])
            for asset_name in version_info[segment]:
                try:
                    new_assets_lst.remove(asset_name)
                except:
                    pass

                version = version_info[segment][asset_name]['version']
                file = version_info[segment][asset_name]['file']

                #- 判断流程版本是否上升
                cur_version_path = ASSETS_PATTERN.format(segment=segment, name=asset_name, version='*').split('*')[0]
                if len(os.listdir(cur_version_path)) > version:
                    latest_file = os.listdir(cur_version_path + VERSION_ARRAY[len(os.listdir(cur_version_path))-1])[-1]
                    new_version_info[segment][asset_name] = {'version':len(os.listdir(cur_version_path)), 'file':latest_file}
                    asset_info = get_asset_info(segment,VERSION_ARRAY[len(os.listdir(cur_version_path))-1],asset_name)
                    copy_to_temp_dir(asset_info[0])
                    copy_to_temp_dir(asset_info[1])
                    continue

                #- 流程版本未上升，判断文件版本是否上升
                latest_file = os.listdir(cur_version_path + VERSION_ARRAY[len(os.listdir(cur_version_path)) - 1])[-1]
                cur_file_version = int(latest_file.split('.')[0].split('_V')[-1])
                file_version = int(file.split('.')[0].split('_V')[-1])
                if cur_file_version>file_version:
                    asset_info = get_asset_info(segment, VERSION_ARRAY[len(os.listdir(cur_version_path)) - 1],asset_name)
                    new_version_info[segment][asset_name] = {'version': version, 'file': latest_file}
                    copy_to_temp_dir(asset_info[0])
                    copy_to_temp_dir(asset_info[1])
                    continue

                #- 文件未更新
                new_version_info[segment][asset_name] = {'version': version, 'file': file}

            #- 新添加的资产
            for asset_name in new_assets_lst:
                asset_path = ASSETS_PATTERN.format(segment=segment, name=asset_name, version='*').split('*')[0]
                latest_version = os.listdir(asset_path)[-1]
                try:
                    asset_info = get_asset_info(segment, latest_version, asset_name)
                    new_version_info[segment][asset_name] = {'version': latest_version, 'file': os.path.basename(asset_info[0])}
                    copy_to_temp_dir(asset_info[0])
                    copy_to_temp_dir(asset_info[1])
                except:
                    print 'failed:'+segment+' '+asset_name
        print new_version_info
        with open(jsonname, 'w') as file:
            json.dump(new_version_info, file)
        #- Mark New Added File

    else:
        new_version_info['ENV'] = dict()
        new_version_info['PROP'] = dict()
        jsonname = os.path.dirname(ASSETS_VERSION_PATTERN) + '/assets_version.json'
        with open(jsonname, 'w') as file:
            json.dump(new_version_info, file)
        split_new_added_assets()


def zip_ya(startdir,file_news):
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('压缩成功')
    z.close()


split_new_added_assets()
#- 是否有新增资产
if os.path.exists(TEMP_DIR_PATTER+'/Project'):
    count = 101
    zip_path = ASSETS_VERSION_PATTERN + 'Submission_' + str(count) + '.zip'
    while os.path.exists(zip_path):
        count += 1
        zip_path = ASSETS_VERSION_PATTERN + 'Submission_' + str(count) + '.zip'
    zip_ya(TEMP_DIR_PATTER+'Project', zip_path)
    shutil.rmtree(TEMP_DIR_PATTER+'/Project')
else:
    print '没有新增资产'