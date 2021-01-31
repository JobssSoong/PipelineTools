import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds
import os,shutil

global CleanUpMod


def CleanUpMod():
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


asset_name = ''


def OnGetAssetGroup(args):
    global asset_name
    asset_name = pm.ls(sl=1, type='transform')[0].name()
    asset_name_field.setFileName(asset_name)
    return asset_name


def OnCleanUp(args):
    CleanUpMod()
    mel.eval('scOpt_performOneCleanup( { "unknownNodesOption" } );')
    op.setEnable(True)
    save_path.setEnable(True)


def OnSegmintChange(args):
    global asset_name
    path = 'E:/Project/Assets/' + op.getValue() + '/' + asset_name + '/layout_model/'
    if os.path.exists(path):
        latest_version = str(os.listdir(path)[-1])
        version = int(latest_version[latest_version.rindex('_')+2:latest_version.rindex('.')])
        save_path.setFileName(path + asset_name + '_V'+str(version+1)+'.ma')
    else:
        save_path.setFileName(path + asset_name + '_V101.ma')
    submit_button.setEnable(True)


def OnSubmit(arges):
    try:
        if not os.path.exists(os.path.dirname(save_path.getFileName())):
            os.makedirs(os.path.dirname(save_path.getFileName()))
        mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "' + save_path.getFileName() + '";')
        #- Create Preview
        p_path = preview_path.getFileName()
        preview_save_path = save_path.getFileName().replace('Assets','Preview').replace('.ma',p_path[p_path.rindex('.'):])
        print type(p_path)
        if not os.path.exists(os.path.dirname(preview_save_path)):
            os.makedirs(os.path.dirname(preview_save_path))
        print preview_save_path
        shutil.copy(p_path,preview_save_path)
        pm.confirmDialog( title='Confirm', message='Success!', button=['666'], defaultButton='Yes')
        submit_button.setEnable(False)
    except:
        pm.confirmDialog( title='Confirm', message='Failed!', button=['555'], defaultButton='Yes')

def OnOpen():
    singleFilter = "All Files (*.*)"
    file_path = str(cmds.fileDialog2(dialogStyle=2, fileMode=1,okCaption='select')[0])
    preview_path.setFileName(file_path)

pm.window('Submit Asset')
pm.columnLayout(columnAttach=('both', 5), rowSpacing=2, columnWidth=350)
pm.text(' ')
pm.rowLayout(numberOfColumns=2, columnWidth2=(220, 25), adjustableColumn=2, columnAlign=(1, 'left'))
asset_name_field = pm.uitypes.TextFieldButtonGrp()
asset_name_field.setFileName(OnGetAssetGroup(''))
get_asset_group = pm.uitypes.Button()
get_asset_group.setLabel('<')
get_asset_group.setCommand(OnGetAssetGroup)
pm.setParent('..')
clean_btn = pm.uitypes.Button()
clean_btn.setLabel('Clean Up')
clean_btn.setCommand(OnCleanUp)
pm.text(' ')
op = pm.uitypes.OptionMenu()
op.setLabel('Segment:')
op.addItems([' ', 'ENV', 'Prop'])
op.changeCommand(OnSegmintChange)
op.setEnable(False)

pm.rowLayout(numberOfColumns=2, columnWidth2=(45,25), adjustableColumn=2, columnAlign=(2, 'left'))
pm.text('SavePath:')
save_path = pm.uitypes.TextFieldButtonGrp()
save_path.setEnableButton(True)
save_path.setEnable(False)
pm.setParent('..')

pm.rowLayout(numberOfColumns=2, columnWidth2=(45,25), adjustableColumn=2, columnAlign=(2, 'left'))
pm.text('Preview:')
preview_path = pm.uitypes.TextFieldButtonGrp()
preview_path.setButtonLabel('Open')
preview_path.setEnableButton(True)
preview_path.adjustableColumn(25)
preview_path.buttonCommand(OnOpen)
pm.setParent('..')

submit_button = pm.uitypes.Button()
submit_button.setLabel('Submit')
submit_button.setEnable(False)
submit_button.setCommand(OnSubmit)
pm.showWindow()
