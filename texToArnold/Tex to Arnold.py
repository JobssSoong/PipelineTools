#- Tex to Arnold

import pymel.core as pm
import os

def create_file_texture():
    _file = pm.shadingNode('file',asTexture=1,isColorManaged=1)
    _coord = pm.shadingNode('place2dTexture',asUtility=1)
    pm.connectAttr(_coord+'.coverage',_file+'.coverage',f=1)
    pm.connectAttr(_coord+'.translateFrame',_file+'.translateFrame',f=1)
    pm.connectAttr(_coord+'.rotateFrame',_file+'.rotateFrame',f=1)
    pm.connectAttr(_coord+'.mirrorU',_file+'.mirrorU',f=1)
    pm.connectAttr(_coord+'.mirrorV',_file+'.mirrorV',f=1)
    pm.connectAttr(_coord+'.stagger',_file+'.stagger',f=1)
    pm.connectAttr(_coord+'.wrapU',_file+'.wrapU',f=1)
    pm.connectAttr(_coord+'.wrapV',_file+'.wrapV',f=1)
    pm.connectAttr(_coord+'.repeatUV',_file+'.repeatUV',f=1)
    pm.connectAttr(_coord+'.offset',_file+'.offset',f=1)
    pm.connectAttr(_coord+'.rotateUV',_file+'.rotateUV',f=1)
    pm.connectAttr(_coord+'.noiseUV',_file+'.noiseUV',f=1)
    pm.connectAttr(_coord+'.vertexUvOne',_file+'.vertexUvOne',f=1)
    pm.connectAttr(_coord+'.vertexUvTwo',_file+'.vertexUvTwo',f=1)
    pm.connectAttr(_coord+'.vertexUvThree',_file+'.vertexUvThree',f=1)
    pm.connectAttr(_coord+'.vertexCameraOne',_file+'.vertexCameraOne',f=1)
    pm.connectAttr(_coord+'.outUV',_file+'.uv',f=1)
    pm.connectAttr(_coord+'.outUvFilterSize',_file+'.uvFilterSize',f=1)
    return _file



img_folder_path = os.path.dirname(pm.sceneName())+'/image'

meshes = pm.ls(sl=1)
ai_material = pm.shadingNode('aiStandardSurface',asShader=1)
pm.select(meshes,r=1)
pm.hyperShade(assign=ai_material)

pm.rename(ai_material,meshes[0].name()+'_MAT')
sg = pm.listConnections(ai_material,type='shadingEngine')[0]
pm.rename(sg,meshes[0].name()+'_SG')

for img_name in os.listdir(img_folder_path):
    file_node = create_file_texture()
    file_node.attr('fileTextureName').set(img_folder_path+'/'+img_name)
    if 'BaseColor' in img_name:
        pm.connectAttr(file_node+'.outColor',ai_material+'.baseColor')
    if 'Roughness' in img_name:
        pm.connectAttr(file_node+'.outAlpha',ai_material+'.specularRoughness')
    if 'Metalness' in img_name:
        pm.connectAttr(file_node+'.outAlpha',ai_material+'.metalness')
    if 'Normal' in img_name:
        pm.connectAttr(file_node+'.outColor',ai_material+'.normalCamera')
