import pymel.core as pm
import maya.mel as mel
import os, shutil
import submitter_env

def CleanUpMod(asset):
    pm.select(asset)
    mel.eval('SelectHierarchy;')
    for i in pm.ls(sl=1, type='mesh'):
        for j in pm.listConnections(i, c=1, p=1, s=1):
            try:
                pm.disconnectAttr(j[0], j[1])
            except:
                pass
            try:
                pm.disconnectAttr(j[1], j[0])
            except:
                pass
    for i in pm.ls(sl=1, type='transform'):
        mel.eval('CenterPivot')
    pm.hyperShade(assign='initialParticleSE')

    unknown_plugins = pm.unknownPlugin(q=True, list=True)
    if unknown_plugins:
        for p in unknown_plugins:
            try:
                pm.unknownPlugin(p, r=True)
                print 'remove', p
            except:
                pass
    print 'Clean Done'


def get_output_path(asset,segment,version):
    path = submitter_env.ASSETS_PATTERN.format(segment=segment, name=asset, version=version)
    if os.path.exists(path):
        latest_version = str(os.listdir(path)[-1])
        version = int(latest_version[latest_version.rindex('_')+2:latest_version.rindex('.')])
        full_path = path + asset + '_V' + str(version+1) + '.ma'
    else:
        full_path = path + asset + '_V101.ma'
    return full_path


def submit_asset(asset, path, is_tex=False):
    try:
        pm.select(asset)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        if is_tex:
            img_folder_path = os.path.dirname(path)+'/image/'+os.path.basename(path).split('.')[0]
            print 'image folder: ' + img_folder_path
            if not os.path.exists(img_folder_path):
                os.makedirs(img_folder_path)
            for f in pm.ls(type='file'):
                img_path = f.attr('fileTextureName').get()
                if os.path.exists(img_path):
                    print '1111',img_path
                    print 'copy image from ({src}) to {dst}'.format(src = img_path, dst=img_folder_path+'/'+os.path.basename(img_path))
                    f.attr('fileTextureName').set(img_folder_path+'/'+os.path.basename(img_path))
                    shutil.copy(img_path, img_folder_path+'/'+os.path.basename(img_path))
        mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "' + path + '";')
        pm.confirmDialog(title='Confirm', message='Success!', button=['666'], defaultButton='Yes')
    except:
        pm.confirmDialog(title='Confirm', message='Failed!', button=['555'], defaultButton='Yes')