import os, sys, json
import loader_env as env


sys.path.append('C:/Python27/Lib/site-packages')
IS_CV2_INSTALLED = 1
try:
    import cv2, numpy
except:
    IS_CV2_INSTALLED = 0


def get_assets_info(segment, version):
    path = env.ASSETS_PATTERN.format(segment=segment, name='*', version=version).split('*')[0]
    p_path = env.PREVIEW_PATTERN.format(segment=segment, name='*', version=version).split('*')[0]
    if not os.path.exists(path) and not os.path.exists(p_path):
        return []

    assets_info = dict()
    for asset in os.listdir(path):
        if os.path.exists(path + asset + '/' + version) and len(os.listdir(path + asset + '/' + version + '/')):
            asset_name = asset
            asset_path = path + asset + '/' + version + '/' + str(os.listdir(path + asset + '/' + version)[-1])
            preview_path = ''
            if os.path.exists(p_path + asset + '/' + version) and len(os.listdir(p_path + asset + '/' + version + '/')):
                lst = os.listdir(p_path + asset + '/' + version)
                for i in lst:
                    if i.endswith('json'):
                        lst.remove(i)
                preview_path = p_path + asset + '/' + version + '/'+ str(lst[-1])
            assets_info[asset_name] = [asset_path, preview_path]
    return assets_info


def load_Reference(path, namespace):
    import maya.mel as mel
    import pymel.core as pm
    count = 1
    final_namespace = namespace + '_' + str(count)
    while pm.namespace(exists=final_namespace):
        count += 1
        final_namespace = namespace + '_' + str(count)
    mel.eval('file -r -type "mayaAscii"  -ignoreVersion -gl -mergeNamespacesOnClash false -namespace "'+final_namespace+'" -options "v=0;" "'+path+'";')


def load_Model(path, namespace):
    import maya.mel as mel
    import pymel.core as pm
    count = 1
    final_namespace = namespace + '_' + str(count)
    while pm.namespace(exists=final_namespace):
        count += 1
        final_namespace = namespace + '_' + str(count)
    mel.eval('file -import -type "mayaAscii"  -ignoreVersion -mergeNamespacesOnClash false -rpr "mod" -options "v=0;" "'+path+'";')


def generate_specipied_preview(path, size):
    if not IS_CV2_INSTALLED:
        print 'CV2 is not installed'
        return False
    if not os.path.isfile(path):
        print 'preview file not exist'
        return False

    print path
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    h = img.shape[0]
    w = img.shape[1]
    if img.shape[2] == 3:
        alpha_channel = numpy.ones((h,w,1))*255
        img = numpy.c_[img, alpha_channel]
        print img.shape
    img_size = img.shape
    if img_size[0] > img_size[1]:
        max_coord = img_size[0]
    else:
        max_coord = img_size[1]
    preview = numpy.zeros([max_coord, max_coord, 4], numpy.uint8)

    x1 = (preview.shape[0] - img.shape[0]) / 2
    y1 = (preview.shape[1] - img.shape[1]) / 2
    x2 = (preview.shape[0] - img.shape[0]) / 2 + img.shape[0]
    y2 = (preview.shape[1] - img.shape[1]) / 2 + img.shape[1]
    preview[x1:x2, y1:y2] = img
    preview = cv2.resize(preview, (size, size))

    cv2.imwrite(os.path.dirname(path)+'/preview.png', preview)

    latest_version = os.path.basename(path)
    jsonname = os.path.dirname(path) + '/preview_version.json'
    with open(jsonname, 'w') as file:
        json.dump(latest_version, file)



