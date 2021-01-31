from PySide2 import QtCore, QtGui, QtWidgets
import shiboken2
import maya.OpenMayaUI as OpenMayaUI
import loader_widgets, loader_utils, loader_env
import os, sys


def get_maya_window():
    window = OpenMayaUI.MQtUtil.mainWindow()
    print shiboken2.wrapInstance(long(window), QtWidgets.QMainWindow)
    return shiboken2.wrapInstance(long(window), QtWidgets.QMainWindow)


class MyItem(QtWidgets.QListWidgetItem):
    def __int__(self):
        super(self).__init__()

    def setInfo(self, name, version, file_path, preview_path):
        self.name = name
        self.version = version
        self.file_path = file_path
        self.preview_path = preview_path

    def getName(self):
        return self.name

    def getFilePath(self):
        return self.file_path

    def getVersion(self):
        return self.version

    def getPreviewPath(self):
        return self.preview_path


class LoaderUI(QtWidgets.QMainWindow, loader_widgets.Ui_MainWindow):
    """

    """

    def __init__(self, parent=get_maya_window()):
        """

        :param parent:
        """
        super(LoaderUI, self).__init__(parent)
        self.setupUi(self)

    def showEvent(self, event):
        self.lst_img_area.setViewMode(QtWidgets.QListView.IconMode)
        self.lst_img_area.setIconSize(QtCore.QSize(200, 200))

    @QtCore.Slot(bool)
    def on_btn_fresh_clicked(self, value):
        self.lst_img_area.clear()
        assets_info = loader_utils.get_assets_info(self.box_segement.currentText(), self.box_version.currentText())
        # - Try Translate Preview into Specipied Size
        import subprocess
        print 'C:/Python27/pythonw.exe '+os.path.dirname(__file__)+'/generate_previews.py'
        subprocess.Popen('C:/Python27/pythonw.exe '+os.path.dirname(__file__)+'/generate_previews.py')

        for name in assets_info:
            icon = QtGui.QIcon()
            if os.path.exists(os.path.dirname(assets_info[name][1])+'/preview.png'):
                icon.addPixmap(QtGui.QPixmap(os.path.dirname(assets_info[name][1]) + '/preview.png'),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                icon.addPixmap(QtGui.QPixmap(assets_info[name][1]),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = MyItem(self.lst_img_area)
            item.setIcon(icon)
            item.setInfo(name, assets_info[name][0].split('_')[-1][:4], assets_info[name][0], assets_info[name][1])
            item.setText(name + ' | ' + assets_info[name][0].split('_')[-1][:4])
        self.lst_img_area.sortItems()
        print assets_info

    @QtCore.Slot(bool)
    def on_btn_load_clicked(self, value):
        loader_utils.load_Model(self.lst_img_area.selectedItems()[0].getFilePath(),
                                self.lst_img_area.selectedItems()[0].getName())
        print self.lst_img_area.selectedItems()[0].getName()

    @QtCore.Slot(bool)
    def on_btn_freshpreview_clicked(self, value):
        assets_info = loader_utils.get_assets_info(self.box_segement.currentText(), self.box_version.currentText())
        for name in assets_info:
            print os.path.dirname(assets_info[name][1]) + '/preview.png'
            if os.path.exists(os.path.dirname(assets_info[name][1]) + '/preview.png'):
                os.remove(os.path.dirname(assets_info[name][1]) + '/preview.png')


def main():
    wnd = LoaderUI()
    wnd.show()
