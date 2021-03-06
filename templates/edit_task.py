# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_task.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 550)
        Dialog.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(223, 223, 200);\n"
"}\n"
"QFrame#main {\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"}")
        self.main = QFrame(Dialog)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 0, 800, 550))
        self.main.setStyleSheet(u"QFrame, QLabel {\n"
"	font-family: Rubik;\n"
"}\n"
"QLabel, QLineEdit {\n"
"	background-color: transparent;\n"
"	color: grey;\n"
"}\n"
"QLabel {\n"
"	font-size:23px;\n"
"	border: 0px;\n"
"	border-radius: 0px;\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 21px;\n"
"	border: 0.5px solid rgba(0, 0, 0, 0.5);\n"
"	border-radius: 10px;\n"
"}")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.save_taskBtn = QPushButton(self.main)
        self.save_taskBtn.setObjectName(u"save_taskBtn")
        self.save_taskBtn.setGeometry(QRect(325, 484, 150, 50))
        self.save_taskBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 255, 127);\n"
"	font-size: 18px;\n"
"	color: black;\n"
"	border: 1px solid grey;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(85, 255, 127, 0.3);\n"
"}")
        self.header = QLabel(self.main)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(320, 10, 181, 31))
        self.header.setStyleSheet(u"color: red;")
        self.exit_button = QPushButton(self.main)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 10, 31, 31))
        self.exit_button.setStyleSheet(u"border: 0px;\n"
"font-size: 20px;")
        self.layoutWidget = QWidget(self.main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 901, 431))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(800, 60))
        self.frame_2.setMaximumSize(QSize(800, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.enter_site_combo_4 = QComboBox(self.frame_2)
        self.enter_site_combo_4.addItem("")
        self.enter_site_combo_4.setObjectName(u"enter_site_combo_4")
        self.enter_site_combo_4.setGeometry(QRect(330, 30, 141, 24))
        self.enter_site_combo_4.setFrame(False)
        self.enter_site_label_4 = QLabel(self.frame_2)
        self.enter_site_label_4.setObjectName(u"enter_site_label_4")
        self.enter_site_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_site_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(800, 60))
        self.frame_3.setMaximumSize(QSize(800, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.enter_profile_combo_4 = QComboBox(self.frame_3)
        self.enter_profile_combo_4.addItem("")
        self.enter_profile_combo_4.setObjectName(u"enter_profile_combo_4")
        self.enter_profile_combo_4.setGeometry(QRect(330, 30, 141, 24))
        self.enter_profile_label_4 = QLabel(self.frame_3)
        self.enter_profile_label_4.setObjectName(u"enter_profile_label_4")
        self.enter_profile_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_profile_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(800, 60))
        self.frame_4.setMaximumSize(QSize(800, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.enter_product_label_4 = QLabel(self.frame_4)
        self.enter_product_label_4.setObjectName(u"enter_product_label_4")
        self.enter_product_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_product_label_4.setAlignment(Qt.AlignCenter)
        self.enter_product_input_4 = QLineEdit(self.frame_4)
        self.enter_product_input_4.setObjectName(u"enter_product_input_4")
        self.enter_product_input_4.setGeometry(QRect(120, 30, 591, 24))
        self.enter_product_input_4.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.layoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(800, 60))
        self.frame_5.setMaximumSize(QSize(800, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.enter_size_combo_4 = QComboBox(self.frame_5)
        self.enter_size_combo_4.addItem("")
        self.enter_size_combo_4.setObjectName(u"enter_size_combo_4")
        self.enter_size_combo_4.setGeometry(QRect(330, 30, 141, 24))
        self.enter_size_label_4 = QLabel(self.frame_5)
        self.enter_size_label_4.setObjectName(u"enter_size_label_4")
        self.enter_size_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_size_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(800, 60))
        self.frame_6.setMaximumSize(QSize(800, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.enter_proxy_label_4 = QLabel(self.frame_6)
        self.enter_proxy_label_4.setObjectName(u"enter_proxy_label_4")
        self.enter_proxy_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_proxy_label_4.setAlignment(Qt.AlignCenter)
        self.enter_proxy_combo_4 = QComboBox(self.frame_6)
        self.enter_proxy_combo_4.addItem("")
        self.enter_proxy_combo_4.setObjectName(u"enter_proxy_combo_4")
        self.enter_proxy_combo_4.setGeometry(QRect(330, 30, 141, 24))

        self.verticalLayout.addWidget(self.frame_6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_taskBtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.header.setText(QCoreApplication.translate("Dialog", u"Edit Task #", None))
        self.exit_button.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.enter_site_combo_4.setItemText(0, QCoreApplication.translate("Dialog", u"Svyaznoy", None))

        self.enter_site_label_4.setText(QCoreApplication.translate("Dialog", u"Site:", None))
        self.enter_profile_combo_4.setItemText(0, QCoreApplication.translate("Dialog", u"Fantic RU", None))

        self.enter_profile_label_4.setText(QCoreApplication.translate("Dialog", u"Profile:", None))
        self.enter_product_label_4.setText(QCoreApplication.translate("Dialog", u"Product:", None))
        self.enter_size_combo_4.setItemText(0, QCoreApplication.translate("Dialog", u"No Size", None))

        self.enter_size_label_4.setText(QCoreApplication.translate("Dialog", u"Size:", None))
        self.enter_proxy_label_4.setText(QCoreApplication.translate("Dialog", u"Proxy:", None))
        self.enter_proxy_combo_4.setItemText(0, QCoreApplication.translate("Dialog", u"Local", None))

    # retranslateUi

