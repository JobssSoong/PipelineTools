# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'submitter_widgetsCegjzw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize,Qt)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 498)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 467, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_assetname = QLineEdit(self.verticalLayoutWidget)
        self.line_assetname.setObjectName("line_assetname")
        self.line_assetname.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.line_assetname)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_getname = QPushButton(self.verticalLayoutWidget)
        self.btn_getname.setObjectName("btn_getname")
        self.btn_getname.setMinimumSize(QSize(30, 30))
        self.btn_getname.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_getname)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.box_segment = QComboBox(self.verticalLayoutWidget)
        self.box_segment.addItem("")
        self.box_segment.addItem("")
        self.box_segment.setObjectName("box_segment")
        self.box_segment.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_4.addWidget(self.box_segment)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.box_version = QComboBox(self.verticalLayoutWidget)
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.setObjectName("box_version")
        self.box_version.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.box_version)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btn_clean = QPushButton(self.verticalLayoutWidget)
        self.btn_clean.setObjectName("btn_clean")
        self.btn_clean.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btn_clean)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.line_outputpath = QLineEdit(self.verticalLayoutWidget)
        self.line_outputpath.setObjectName("line_outputpath")
        self.line_outputpath.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.line_outputpath)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")

        self.horizontalLayout_5.addWidget(self.listWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_grabscreen = QPushButton(self.verticalLayoutWidget)
        self.btn_grabscreen.setObjectName("btn_grabscreen")
        self.btn_grabscreen.setMinimumSize(QSize(0, 45))

        self.verticalLayout_2.addWidget(self.btn_grabscreen)

        self.btn_remove = QPushButton(self.verticalLayoutWidget)
        self.btn_remove.setObjectName("btn_remove")
        self.btn_remove.setMinimumSize(QSize(0, 45))

        self.verticalLayout_2.addWidget(self.btn_remove)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.btn_submit = QPushButton(self.verticalLayoutWidget)
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.btn_submit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Submitter", None))
        self.btn_getname.setText(QCoreApplication.translate("MainWindow", "<", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Segment:", None))
        self.box_segment.setItemText(0, QCoreApplication.translate("MainWindow", "ENV", None))
        self.box_segment.setItemText(1, QCoreApplication.translate("MainWindow", "PROP", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", "    Version:", None))
        self.box_version.setItemText(0, QCoreApplication.translate("MainWindow", "layout_model", None))
        self.box_version.setItemText(1, QCoreApplication.translate("MainWindow", "correct_model", None))
        self.box_version.setItemText(2, QCoreApplication.translate("MainWindow", "high_model", None))
        self.box_version.setItemText(3, QCoreApplication.translate("MainWindow", "tex", None))

        self.btn_clean.setText(QCoreApplication.translate("MainWindow", "clean up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Output path:  ", None))
        self.btn_grabscreen.setText(QCoreApplication.translate("MainWindow", "Grab Screen", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", "Remove", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", "Submit", None))
    # retranslateUi

