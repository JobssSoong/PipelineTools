#- to TEX export

import pymel.core as pm
import maya.cmds as cmds
import os

asset_name = pm.ls(sl=1)[0].name()
pm.duplicate(rr=1)
pm.move([-30,0,0],r=1)
pm.select(hierarchy=1)
for i in pm.ls(sl=1):
    if i.type()=='mesh':
        pm.polySmooth(i)
        
fbx_path = os.path.dirname(pm.sceneName())+'/'+asset_name+'_totex.fbx'
cmds.file(fbx_path,force=1, options="v=0;" ,typ="FBX export" ,pr=1 ,es=1)

trans_node = pm.ls(sl=1,type='transform')[0]
pm.select(trans_node)
pm.delete()