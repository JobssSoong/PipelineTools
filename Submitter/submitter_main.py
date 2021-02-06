from PySide2 import QtCore, QtGui, QtWidgets
import shiboken2
import maya.OpenMayaUI as OpenMayaUI
import submitter_widgets, submitter_utils, submitter_env, screen_grab
import os, sys
import pymel.core as pm


def get_maya_window():
    window = OpenMayaUI.MQtUtil.mainWindow()
    print shiboken2.wrapInstance(long(window), QtWidgets.QMainWindow)
    return shiboken2.wrapInstance(long(window), QtWidgets.QMainWindow)


class SubmitterUI(QtWidgets.QMainWindow, submitter_widgets.Ui_MainWindow):
    """

    """

    def __init__(self, parent=get_maya_window()):
        """

        :param parent:
        """

        super(SubmitterUI, self).__init__(parent)
        self.setupUi(self)
        self.line_outputpath.setDisabled(True)
        self.btn_grabscreen.setDisabled(True)
        self.btn_remove.setDisabled(True)
        self.btn_submit.setDisabled(True)
        self.asset = pm.ls(sl=True)[0]
        self.line_assetname.setText(str(self.asset))
        self.has_pic = False


    @QtCore.Slot(bool)
    def on_btn_getname_clicked(self, value):
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(300, 300))
        self.asset = pm.ls(sl=True)[0]
        self.line_assetname.setText(str(pm.ls(sl=True)[0]))
        self.btn_grabscreen.setDisabled(True)
        self.btn_remove.setDisabled(True)

    @QtCore.Slot(bool)
    def on_btn_clean_clicked(self, value):
        self.btn_grabscreen.setEnabled(True)
        self.btn_remove.setEnabled(True)
        submitter_utils.CleanUpMod(self.asset)
        out_path = submitter_utils.get_output_path(self.asset, self.box_segment.currentText(),
                                                   self.box_version.currentText())
        self.line_outputpath.setText(out_path)

    @QtCore.Slot(str)
    def on_box_segment_currentTextChanged(self, value):
        out_path = submitter_utils.get_output_path(self.asset, self.box_segment.currentText(),
                                                   self.box_version.currentText())
        self.line_outputpath.setText(out_path)

    @QtCore.Slot(str)
    def on_box_version_currentTextChanged(self, value):
        out_path = submitter_utils.get_output_path(self.asset, self.box_segment.currentText(),
                                                   self.box_version.currentText())
        self.line_outputpath.setText(out_path)
        print value
        if value == 'tex':
            self.btn_clean.setDisabled(True)
            self.btn_grabscreen.setEnabled(True)
            self.btn_remove.setEnabled(True)
        else:
            self.btn_clean.setEnabled(True)

    @QtCore.Slot(bool)
    def on_btn_grabscreen_clicked(self, value):
        if not self.has_pic:
            self.has_pic = True
            try:
                p = screen_grab.ScreenGrabber(self)
                if p:
                    self.q_pix_img = p.screen_capture()
                    icon = QtGui.QIcon()
                    icon.addPixmap(self.q_pix_img, QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item = QtWidgets.QListWidgetItem(self.listWidget)
                    item.setIcon(icon)
                    self.btn_submit.setEnabled(True)
            except:
                pass

    @QtCore.Slot(bool)
    def on_btn_remove_clicked(self, value):
        self.listWidget.clear()
        self.has_pic = False
        self.btn_submit.setDisabled(True)

    @QtCore.Slot(bool)
    def on_btn_submit_clicked(self, value):
        preview_path = submitter_env.PREVIEW_PATTERN.format(segment=self.box_segment.currentText(),name=str(self.asset),version=self.box_version.currentText())
        preview_path = preview_path + self.line_outputpath.text()[self.line_outputpath.text().rindex('/'):self.line_outputpath.text().rindex('.')]+'.png'
        print preview_path
        if not os.path.exists(os.path.dirname(preview_path)):
            os.makedirs(os.path.dirname(preview_path))
        self.q_pix_img.save(preview_path)
        if self.box_version.currentText() == 'tex':
            submitter_utils.submit_asset(self.asset, self.line_outputpath.text(), is_tex=True)
        else:
            submitter_utils.submit_asset(self.asset, self.line_outputpath.text())

def main():
    wnd = SubmitterUI()
    wnd.show()

    return wnd
