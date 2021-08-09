# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from edit_task import Ui_Dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"CenturionAIO")
        MainWindow.resize(1024, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget, QFrame#tab_bar {\n"
"	border: 1px solid black;\n"
"	border-radius: 20px;\n"
"}\n"
"QWidget#centralwidget {\n"
"	background-color: rgb(245,245,220);\n"
"}")
        self.tab_bar = QFrame(self.centralwidget)
        self.tab_bar.setObjectName(u"tab_bar")
        self.tab_bar.setGeometry(QRect(0, 0, 1024, 80))
        self.tab_bar.setStyleSheet(u"QPushButton {\n"
"	font-size: 25px;\n"
"	border: 0.5px solid rgba(0, 0, 0, 0.5);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QFrame, QPushButton {\n"
"	background-color: rgb(255, 125, 105);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 0px;\n"
"}\n"
"QPushButton#exit_button:hover, QPushButton#hide_button:hover {\n"
"	background-color: rgba(0, 0, 0 ,0.3);\n"
"}")
        self.tab_bar.setFrameShape(QFrame.StyledPanel)
        self.tab_bar.setFrameShadow(QFrame.Raised)
        self.icon = QLabel(self.tab_bar)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(10, 10, 60, 60))
        self.icon.setPixmap(QPixmap(u"img/icon.svg"))
        self.task_creator = QPushButton(self.tab_bar)
        self.task_creator.setObjectName(u"task_creator")
        self.task_creator.setGeometry(QRect(100, 15, 150, 50))
        self.tasks = QPushButton(self.tab_bar)
        self.tasks.setObjectName(u"tasks")
        self.tasks.setGeometry(QRect(280, 15, 100, 50))
        self.billing = QPushButton(self.tab_bar)
        self.billing.setObjectName(u"billing")
        self.billing.setGeometry(QRect(410, 15, 120, 50))
        self.proxies = QPushButton(self.tab_bar)
        self.proxies.setObjectName(u"proxies")
        self.proxies.setGeometry(QRect(560, 15, 120, 50))
        self.settings = QPushButton(self.tab_bar)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(710, 15, 140, 50))
        self.exit_button = QPushButton(self.tab_bar)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(970, 22, 31, 31))
        self.exit_button.setStyleSheet(u"border: 0px;\n"
"font-size: 20px;")
        self.hide_button = QPushButton(self.tab_bar)
        self.hide_button.setObjectName(u"hide_button")
        self.hide_button.setGeometry(QRect(940, 21, 31, 31))
        self.hide_button.setStyleSheet(u"border: 0px;\n"
"font-size: 50px;")
        self.tabs_widget = QStackedWidget(self.centralwidget)
        self.tabs_widget.setObjectName(u"tabs_widget")
        self.tabs_widget.setGeometry(QRect(30, 100, 994, 668))
        self.tabs_widget.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.task_creator_tab = QWidget()
        self.task_creator_tab.setObjectName(u"task_creator_tab")
        self.task_creator_tab.setStyleSheet(u"font-family: Rubik;")
        self.task_creator_frame = QFrame(self.task_creator_tab)
        self.task_creator_frame.setObjectName(u"task_creator_frame")
        self.task_creator_frame.setGeometry(QRect(0, 0, 964, 571))
        self.task_creator_frame.setStyleSheet(u"QFrame#task_creator_frame {\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
"}\n"
"QFrame, QLabel {\n"
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
        self.task_creator_frame.setFrameShape(QFrame.StyledPanel)
        self.task_creator_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.task_creator_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 955, 551))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 10, 0, 0)
        self.site_frame = QFrame(self.layoutWidget)
        self.site_frame.setObjectName(u"site_frame")
        self.site_frame.setMinimumSize(QSize(944, 80))
        self.site_frame.setFrameShape(QFrame.StyledPanel)
        self.site_frame.setFrameShadow(QFrame.Raised)
        self.enter_site_label = QLabel(self.site_frame)
        self.enter_site_label.setObjectName(u"enter_site_label")
        self.enter_site_label.setGeometry(QRect(0, -5, 141, 31))
        self.enter_site_combo = QComboBox(self.site_frame)
        self.enter_site_combo.addItem("")
        self.enter_site_combo.setObjectName(u"enter_site_combo")
        self.enter_site_combo.setGeometry(QRect(0, 46, 141, 31))

        self.verticalLayout.addWidget(self.site_frame)

        self.profile_frame = QFrame(self.layoutWidget)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setMinimumSize(QSize(944, 80))
        self.profile_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QFrame.Raised)
        self.enter_profile_combo = QComboBox(self.profile_frame)
        self.enter_profile_combo.addItem("")
        self.enter_profile_combo.setObjectName(u"enter_profile_combo")
        self.enter_profile_combo.setGeometry(QRect(0, 46, 141, 31))
        self.enter_profile_label = QLabel(self.profile_frame)
        self.enter_profile_label.setObjectName(u"enter_profile_label")
        self.enter_profile_label.setGeometry(QRect(0, 0, 141, 31))

        self.verticalLayout.addWidget(self.profile_frame)

        self.product_frame = QFrame(self.layoutWidget)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setMinimumSize(QSize(944, 80))
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.enter_product_label = QLabel(self.product_frame)
        self.enter_product_label.setObjectName(u"enter_product_label")
        self.enter_product_label.setGeometry(QRect(0, 0, 141, 31))
        self.enter_product_input = QLineEdit(self.product_frame)
        self.enter_product_input.setObjectName(u"enter_product_input")
        self.enter_product_input.setGeometry(QRect(0, 46, 940, 31))
        self.enter_product_input.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.product_frame)

        self.size_frame = QFrame(self.layoutWidget)
        self.size_frame.setObjectName(u"size_frame")
        self.size_frame.setMinimumSize(QSize(944, 80))
        self.size_frame.setFrameShape(QFrame.StyledPanel)
        self.size_frame.setFrameShadow(QFrame.Raised)
        self.enter_size_label = QLabel(self.size_frame)
        self.enter_size_label.setObjectName(u"enter_size_label")
        self.enter_size_label.setGeometry(QRect(0, 0, 141, 31))
        self.enter_size_combo = QComboBox(self.size_frame)
        self.enter_size_combo.addItem("")
        self.enter_size_combo.setObjectName(u"enter_size_combo")
        self.enter_size_combo.setGeometry(QRect(0, 46, 141, 31))

        self.verticalLayout.addWidget(self.size_frame)

        self.proxy_frame_ = QFrame(self.layoutWidget)
        self.proxy_frame_.setObjectName(u"proxy_frame_")
        self.proxy_frame_.setMinimumSize(QSize(944, 80))
        self.proxy_frame_.setFrameShape(QFrame.StyledPanel)
        self.proxy_frame_.setFrameShadow(QFrame.Raised)
        self.enter_proxy_label = QLabel(self.proxy_frame_)
        self.enter_proxy_label.setObjectName(u"enter_proxy_label")
        self.enter_proxy_label.setGeometry(QRect(0, 0, 141, 31))
        self.enter_proxy_combo = QComboBox(self.proxy_frame_)
        self.enter_proxy_combo.addItem("")
        self.enter_proxy_combo.setObjectName(u"enter_proxy_combo")
        self.enter_proxy_combo.setGeometry(QRect(0, 46, 141, 31))

        self.verticalLayout.addWidget(self.proxy_frame_)

        self.add_taskBtn = QPushButton(self.task_creator_tab)
        self.add_taskBtn.setObjectName(u"add_taskBtn")
        self.add_taskBtn.setGeometry(QRect(0, 590, 151, 51))
        self.add_taskBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(157, 157, 157);\n"
"	font-size: 18px;\n"
"	color: white;\n"
"	border: 1px solid grey;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(157, 157, 157, 0.7);\n"
"}")
        self.tabs_widget.addWidget(self.task_creator_tab)
        self.tasks_tab = QWidget()
        self.tasks_tab.setObjectName(u"tasks_tab")
        self.tasks_tab.setStyleSheet(u"")
        self.tasks_frame = QFrame(self.tasks_tab)
        self.tasks_frame.setObjectName(u"tasks_frame")
        self.tasks_frame.setGeometry(QRect(0, 0, 964, 571))
        self.tasks_frame.setStyleSheet(u"QFrame#tasks_frame {\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
"}\n"
"QFrame, QLabel {\n"
"	font-family: Rubik;\n"
"}")
        self.tasks_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QFrame.Raised)
        self.collumns = QFrame(self.tasks_frame)
        self.collumns.setObjectName(u"collumns")
        self.collumns.setGeometry(QRect(10, 10, 944, 40))
        self.collumns.setStyleSheet(u"QFrame {\n"
"	border: 0px;\n"
"}\n"
"QLabel {\n"
"	font-family: Rubik;\n"
"	font-size: 20px;\n"
"	color: grey;\n"
"}")
        self.collumns.setFrameShape(QFrame.StyledPanel)
        self.collumns.setFrameShadow(QFrame.Raised)
        self.num_collumn = QLabel(self.collumns)
        self.num_collumn.setObjectName(u"num_collumn")
        self.num_collumn.setGeometry(QRect(11, 6, 24, 24))
        self.site_collumn = QLabel(self.collumns)
        self.site_collumn.setObjectName(u"site_collumn")
        self.site_collumn.setGeometry(QRect(50, 6, 91, 24))
        self.site_collumn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.profile_collumn = QLabel(self.collumns)
        self.profile_collumn.setObjectName(u"profile_collumn")
        self.profile_collumn.setGeometry(QRect(405, 6, 81, 24))
        self.product_collumn = QLabel(self.collumns)
        self.product_collumn.setObjectName(u"product_collumn")
        self.product_collumn.setGeometry(QRect(150, 6, 161, 24))
        self.size_collumn = QLabel(self.collumns)
        self.size_collumn.setObjectName(u"size_collumn")
        self.size_collumn.setGeometry(QRect(330, 6, 61, 24))
        self.proxy_collumn = QLabel(self.collumns)
        self.proxy_collumn.setObjectName(u"proxy_collumn")
        self.proxy_collumn.setGeometry(QRect(500, 6, 60, 24))
        self.status_collumn = QLabel(self.collumns)
        self.status_collumn.setObjectName(u"status_collumn")
        self.status_collumn.setGeometry(QRect(580, 6, 191, 24))
        self.status_collumn.setAlignment(Qt.AlignCenter)
        self.actions_collumn = QLabel(self.collumns)
        self.actions_collumn.setObjectName(u"actions_collumn")
        self.actions_collumn.setGeometry(QRect(780, 6, 161, 24))
        self.actions_collumn.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.tasks_frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 60, 964, 500))
        self.listWidget.setStyleSheet(u"QListWidget::item {\n"
"	background-color: rgba(0, 0, 0, 0.2);\n"
"	border: 0.1px solid transparent;\n"
"	border-radius: 12px;\n"
"}\n"
"QListWidget {\n"
"	border: 0px;\n"
"}\n"
"QLabel {\n"
"	background-color: transparent;\n"
"	font-size: 17px;\n"
"	font-family: Rubik;\n"
"	color: rgb(235, 235, 235);\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	border-radius: 0px;\n"
"}")
        self.listWidget.setSpacing(3)
        self.listWidget.raise_()
        self.collumns.raise_()
        self.tabs_widget.addWidget(self.tasks_tab)
        self.billing_tab = QWidget()
        self.billing_tab.setObjectName(u"billing_tab")
        self.billing_frame = QFrame(self.billing_tab)
        self.billing_frame.setObjectName(u"billing_frame")
        self.billing_frame.setGeometry(QRect(0, 0, 964, 571))
        self.billing_frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
"}\n"
"QFrame, QLabel {\n"
"	font-family: Rubik;\n"
"}")
        self.billing_frame.setFrameShape(QFrame.StyledPanel)
        self.billing_frame.setFrameShadow(QFrame.Raised)
        self.tabs_widget.addWidget(self.billing_tab)
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.settings_tab.setStyleSheet(u"QLabel, QLineEdit, QPushButton {\n"
"	font-family: Rubik;\n"
"}\n"
"QPushButton {\n"
"	font-size: 20px;\n"
"	border: 0.5px solid rgba(0, 0, 0, 0.3);\n"
"	border-radius: 10px;\n"
"}")
        self.settings_frame = QFrame(self.settings_tab)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(0, 0, 964, 571))
        self.settings_frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
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
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.webhook_label = QLabel(self.settings_frame)
        self.webhook_label.setObjectName(u"webhook_label")
        self.webhook_label.setGeometry(QRect(10, 15, 211, 31))
        self.webhook_input = QLineEdit(self.settings_frame)
        self.webhook_input.setObjectName(u"webhook_input")
        self.webhook_input.setGeometry(QRect(10, 60, 944, 35))
        self.webhook_input.setCursorPosition(0)
        self.save_settings_button = QPushButton(self.settings_tab)
        self.save_settings_button.setObjectName(u"save_settings_button")
        self.save_settings_button.setGeometry(QRect(0, 600, 141, 41))
        self.save_settings_button.setStyleSheet(u"background-color: rgba(0, 255, 0, 0.4);")
        self.save_indicator = QLabel(self.settings_tab)
        self.save_indicator.setObjectName(u"save_indicator")
        self.save_indicator.setGeometry(QRect(0, 576, 141, 20))
        self.save_indicator.setStyleSheet(u"color: green;\n"
"font-size: 17px;")
        self.test_webhook_button = QPushButton(self.settings_tab)
        self.test_webhook_button.setObjectName(u"test_webhook_button")
        self.test_webhook_button.setGeometry(QRect(170, 600, 161, 41))
        self.test_webhook_button.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.tabs_widget.addWidget(self.settings_tab)
        self.proxies_tab = QWidget()
        self.proxies_tab.setObjectName(u"proxies_tab")
        self.frame = QFrame(self.proxies_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 964, 571))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
"}\n"
"QFrame, QLabel {\n"
"	font-family: Rubik;\n"
"}")
        self.tasks_num = 0
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabs_widget.addWidget(self.proxies_tab)

        self.pos = MainWindow.pos()
        self.tasks_container = dict()
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(lambda: MainWindow.close())
        self.hide_button.clicked.connect(lambda: MainWindow.showMinimized())
        self.task_creator.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(0))
        self.tasks.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(1))
        self.billing.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(2))
        self.proxies.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(4))
        self.settings.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(3))

        
        self.add_taskBtn.clicked.connect(self.add_task)

        self.save_indicator.hide()

        self.retranslateUi(MainWindow)

        self.tabs_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def add_task(self):
        data = dict()
        self.tasks_num += 1
        data['num'] = str(self.tasks_num)
        data['site'] = self.enter_site_combo.currentText()
        data['profile'] = self.enter_profile_combo.currentText()
        data['product'] = self.enter_product_input.text()
        data['size'] = self.enter_size_combo.currentText()
        data['proxy'] = self.enter_proxy_combo.currentText()
        item = QListWidgetItem(self.listWidget)
        item.setSizeHint(QSize(944, 40))
        data['item'] = item
        widget = taskWidget(item, data)
        widget.itemDeleted.connect(self.deleteTask)
        widget.itemEdited.connect(self.editTask)
        # Binding delete signal
        self.listWidget.setItemWidget(item, widget)

        self.tasks_container[self.tasks_num] = data

        del data
    
    def deleteTask(self, item):
        row = self.listWidget.indexFromItem(item).row()
        item = self.listWidget.takeItem(row)
        self.listWidget.removeItemWidget(item)
        del item

    def editTask(self, item):
        print(item)
        for t in self.tasks_container:
            if self.tasks_container[t]['item'] == item:
                break
        
        dialog = Ui_Dialog(self.tasks_container[t])
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        dialog.move(center.x()-400, center.y()-275)
        if dialog.exec() == QDialog.Accepted:
            print('edited')
        else:
            print('cancelled')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.task_creator.setText(QCoreApplication.translate("MainWindow", u"Task Creator", None))
        self.tasks.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.billing.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.proxies.setText(QCoreApplication.translate("MainWindow", u"Proxies", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.hide_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.enter_site_label.setText(QCoreApplication.translate("MainWindow", u"Site:", None))
        self.enter_site_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Svyaznoy", None))

        self.enter_profile_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Fantic RU", None))

        self.enter_profile_label.setText(QCoreApplication.translate("MainWindow", u"Profile:", None))
        self.enter_product_label.setText(QCoreApplication.translate("MainWindow", u"Product:", None))
        self.enter_size_label.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.enter_size_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"No Size", None))

        self.enter_proxy_label.setText(QCoreApplication.translate("MainWindow", u"Proxy:", None))
        self.enter_proxy_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Local", None))

        self.add_taskBtn.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.num_collumn.setText(QCoreApplication.translate("MainWindow", u"\u2116", None))
        self.site_collumn.setText(QCoreApplication.translate("MainWindow", u"Site", None))
        self.profile_collumn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.product_collumn.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.size_collumn.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.proxy_collumn.setText(QCoreApplication.translate("MainWindow", u"Proxy", None))
        self.status_collumn.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.actions_collumn.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.webhook_label.setText(QCoreApplication.translate("MainWindow", u"Discord Webhook:", None))
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_indicator.setText(QCoreApplication.translate("MainWindow", u"saved!", None))
        self.test_webhook_button.setText(QCoreApplication.translate("MainWindow", u"Test Webhook", None))
    # retranslateUi

class taskWidget(QWidget):
    itemDeleted = Signal(QListWidgetItem)
    itemEdited = Signal(QListWidgetItem)
    def __init__(self, item, data, *args, **kwargs):
        super(taskWidget, self).__init__(*args, **kwargs)
        self._item = item
        self.num_row = QLabel(self)
        self.num_row.setObjectName(u"num_row")
        self.num_row.setGeometry(QRect(9, 9, 24, 24))
        self.num_row.setAlignment(Qt.AlignCenter)
        self.site_row = QLabel(self)
        self.site_row.setObjectName(u"site_row")
        self.site_row.setGeometry(QRect(50, 9, 91, 24))
        self.product_row = QLabel(self)
        self.product_row.setObjectName(u"product_row")
        self.product_row.setGeometry(QRect(150, 9, 161, 24))
        self.size_row = QLabel(self)
        self.size_row.setObjectName(u"size_row")
        self.size_row.setGeometry(QRect(330, 9, 61, 24))
        self.profile_row = QLabel(self)
        self.profile_row.setObjectName(u"profile_row")
        self.profile_row.setGeometry(QRect(405, 9, 81, 24))
        self.proxy_row = QLabel(self)
        self.proxy_row.setObjectName(u"proxy_row")
        self.proxy_row.setGeometry(QRect(500, 9, 60, 24))
        self.status_row = QLabel(self)
        self.status_row.setObjectName(u"status_row")
        self.status_row.setGeometry(QRect(580, 9, 191, 24))
        self.status_row.setAlignment(Qt.AlignCenter)
        self.start_row = QPushButton(self)
        self.start_row.setObjectName(u"start_row")
        self.start_row.setGeometry(QRect(781, 6, 26, 26))
        icon1 = QIcon()
        icon1.addFile(u"img/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_row.setIcon(icon1)
        self.start_row.setIconSize(QSize(26, 26))
        self.stop_row = QPushButton(self)
        self.stop_row.setObjectName(u"stop_row")
        self.stop_row.setGeometry(QRect(820, 6, 26, 26))
        icon2 = QIcon()
        icon2.addFile(u"img/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_row.setIcon(icon2)
        self.stop_row.setIconSize(QSize(26, 26))
        self.edit_row = QPushButton(self)
        self.edit_row.setObjectName(u"edit_row")
        self.edit_row.setGeometry(QRect(860, 6, 26, 26))
        icon3 = QIcon()
        icon3.addFile(u"img/pen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_row.setIcon(icon3)
        self.edit_row.setIconSize(QSize(26, 26))
        self.delete_row = QPushButton(self)
        self.delete_row.setObjectName(u"delete_row")
        self.delete_row.setGeometry(QRect(900, 6, 26, 26))

        self.delete_row.clicked.connect(self.deleteItem)
        self.edit_row.clicked.connect(self.editItem)

        icon4 = QIcon()
        icon4.addFile(u"img/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_row.setIcon(icon4)
        self.delete_row.setIconSize(QSize(26, 26))
        self.num_row.setText(QCoreApplication.translate("MainWindow", data['num'], None))
        self.site_row.setText(QCoreApplication.translate("MainWindow", data['site'], None))
        self.product_row.setText(QCoreApplication.translate("MainWindow", data['product'], None))
        self.size_row.setText(QCoreApplication.translate("MainWindow", data['size'], None))
        self.profile_row.setText(QCoreApplication.translate("MainWindow", data['profile'], None))
        self.proxy_row.setText(QCoreApplication.translate("MainWindow", data['proxy'], None))
        self.status_row.setText(QCoreApplication.translate("MainWindow", u"stopped", None))

    def deleteItem(self):
        self.itemDeleted.emit(self._item)

    def editItem(self):
        self.itemEdited.emit(self._item)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    Form = QMainWindow()
    # Create and show the form
    login = Ui_MainWindow()
    login.setupUi(Form)
    Form.show()
    # Run the main Qt loop
    sys.exit(app.exec())