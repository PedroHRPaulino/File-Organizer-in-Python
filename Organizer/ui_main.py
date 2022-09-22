# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 70, 511, 351))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, -1)
        self.txt_path = QLineEdit(self.frame)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setTabletTracking(False)
        self.txt_path.setAutoFillBackground(False)
        self.txt_path.setCursorPosition(0)
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy1)
        self.btn_open.setMinimumSize(QSize(120, 28))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_open.setFont(font)
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"background-color: rgb(234,234,234)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#fff;\n"
"background-color: rgb(0,167,235)\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_4)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_organize.sizePolicy().hasHeightForWidth())
        self.btn_organize.setSizePolicy(sizePolicy2)
        self.btn_organize.setMinimumSize(QSize(200, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.btn_organize.setFont(font1)
        self.btn_organize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_organize.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(234,234,234);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#fff;\n"
"background-color: rgb(0,157,235)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_organize)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/imgs/icone.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#0037a5;\">FILE ORGANIZE</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_4.setText("")
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.label_3.setText("")
    # retranslateUi

