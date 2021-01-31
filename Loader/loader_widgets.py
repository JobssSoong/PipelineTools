# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loader_widgetsrdmnqg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1163, 653)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.box_segement = QComboBox(self.centralwidget)
        self.box_segement.addItem("")
        self.box_segement.addItem("")
        self.box_segement.setObjectName("box_segement")
        font1 = QFont()
        font1.setFamily("Arial")
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.box_segement.setFont(font1)

        self.horizontalLayout.addWidget(self.box_segement)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.box_version = QComboBox(self.centralwidget)
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.addItem("")
        self.box_version.setObjectName("box_version")
        self.box_version.setMinimumSize(QSize(100, 0))
        self.box_version.setFont(font1)

        self.horizontalLayout_2.addWidget(self.box_version)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_fresh = QPushButton(self.centralwidget)
        self.btn_fresh.setObjectName("btn_fresh")
        self.btn_fresh.setMinimumSize(QSize(0, 30))
        self.btn_fresh.setFont(font1)

        self.horizontalLayout_5.addWidget(self.btn_fresh)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.lst_img_area = QListWidget(self.centralwidget)
        self.lst_img_area.setObjectName("lst_img_area")

        self.gridLayout.addWidget(self.lst_img_area, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_freshpreview = QPushButton(self.centralwidget)
        self.btn_freshpreview.setObjectName("btn_freshpreview")
        self.btn_freshpreview.setMinimumSize(QSize(40, 40))
        self.btn_freshpreview.setFont(font1)

        self.horizontalLayout_6.addWidget(self.btn_freshpreview)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setMinimumSize(QSize(100, 30))
        self.btn_load.setFont(font1)

        self.horizontalLayout_6.addWidget(self.btn_load)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Loader", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "  Segement:", None))
        self.box_segement.setItemText(0, QCoreApplication.translate("MainWindow", "ENV", None))
        self.box_segement.setItemText(1, QCoreApplication.translate("MainWindow", "PROP", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", "  Version: ", None))
        self.box_version.setItemText(0, QCoreApplication.translate("MainWindow", "layout_model", None))
        self.box_version.setItemText(1, QCoreApplication.translate("MainWindow", "correct_model", None))
        self.box_version.setItemText(2, QCoreApplication.translate("MainWindow", "high_model", None))
        self.box_version.setItemText(3, QCoreApplication.translate("MainWindow", "tex", None))

        self.btn_fresh.setText(QCoreApplication.translate("MainWindow", "Fresh", None))
        self.btn_freshpreview.setText(QCoreApplication.translate("MainWindow", "Fresh Generated Preview", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", "Load", None))
    # retranslateUi

