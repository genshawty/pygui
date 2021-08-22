from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Dialog(QDialog):
    itemEdit = Signal(dict)
    def __init__(self, data, profiles, proxies):
        self.profiles_container = profiles
        self.proxies_container = proxies
        self.data = data
        super(Ui_Dialog, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        if not self.objectName():
            self.setObjectName(u"Edit Task")
        self.resize(800, 550)
        self.setStyleSheet('''QFrame {
	background-color: rgb(223, 223, 200);
}
QFrame#main {
	border: 2px solid grey;
	border-radius: 10px;
}
QComboBox {
	background-color: transparent;
	selection-background-color: transparent;
	selection-color: black;
}''')
        self.main = QFrame(self)
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
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(795, 60))
        self.frame_2.setMaximumSize(QSize(795, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.enter_site_combo = QComboBox(self.frame_2)
        self.enter_site_combo.addItem("")
        self.enter_site_combo.setObjectName(u"enter_site_combo")
        self.enter_site_combo.setGeometry(QRect(330, 30, 141, 24))
        self.enter_site_combo.setFrame(False)
        self.enter_site_label_4 = QLabel(self.frame_2)
        self.enter_site_label_4.setObjectName(u"enter_site_label_4")
        self.enter_site_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_site_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(795, 60))
        self.frame_3.setMaximumSize(QSize(795, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.enter_profile_combo = QComboBox(self.frame_3)

        self.enter_profile_combo.setObjectName(u"enter_profile_combo")
        self.enter_profile_combo.setGeometry(QRect(330, 30, 141, 24))
        self.enter_profile_label_4 = QLabel(self.frame_3)
        self.enter_profile_label_4.setObjectName(u"enter_profile_label_4")
        self.enter_profile_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_profile_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(795, 60))
        self.frame_4.setMaximumSize(QSize(795, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.enter_product_label_4 = QLabel(self.frame_4)
        self.enter_product_label_4.setObjectName(u"enter_product_label_4")
        self.enter_product_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_product_label_4.setAlignment(Qt.AlignCenter)
        self.enter_product_input = QLineEdit(self.frame_4)
        self.enter_product_input.setObjectName(u"enter_product_input")
        self.enter_product_input.setGeometry(QRect(120, 30, 591, 24))
        self.enter_product_input.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.layoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(795, 60))
        self.frame_5.setMaximumSize(QSize(795, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.enter_size_combo = QComboBox(self.frame_5)
        self.enter_size_combo.addItem("")
        self.enter_size_combo.setObjectName(u"enter_size_combo")
        self.enter_size_combo.setGeometry(QRect(330, 30, 141, 24))
        self.enter_size_label_4 = QLabel(self.frame_5)
        self.enter_size_label_4.setObjectName(u"enter_size_label_4")
        self.enter_size_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_size_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(795, 60))
        self.frame_6.setMaximumSize(QSize(795, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.enter_proxy_label_4 = QLabel(self.frame_6)
        self.enter_proxy_label_4.setObjectName(u"enter_proxy_label_4")
        self.enter_proxy_label_4.setGeometry(QRect(330, 0, 141, 31))
        self.enter_proxy_label_4.setAlignment(Qt.AlignCenter)
        self.enter_proxy_combo = QComboBox(self.frame_6)

        self.enter_proxy_combo.setObjectName(u"enter_proxy_combo")
        self.enter_proxy_combo.setGeometry(QRect(330, 30, 141, 24))

        self.verticalLayout.addWidget(self.frame_6)

        self.exit_button.clicked.connect(self.close)
        self.save_taskBtn.clicked.connect(self.save_task)
        self.retranslateUi()
        self.update_comboboxes()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def update_comboboxes(self):  
        names = list(self.profiles_container.keys())
        for i in range(self.enter_profile_combo.count()):
            self.enter_profile_combo.removeItem(0)
            
        for i in range(len(names)):
            self.enter_profile_combo.addItem(names[i])
    
        names = list(self.proxies_container.keys())
        for i in range(self.enter_proxy_combo.count()):
            self.enter_proxy_combo.removeItem(0)
        for i in range(len(names)):
            self.enter_proxy_combo.addItem(names[i])

    def save_task(self):
        self.data['site'] = self.enter_site_combo.currentText()
        self.data['profile'] = self.enter_profile_combo.currentText()
        self.data['product'] = self.enter_product_input.text()
        self.data['size'] = self.enter_size_combo.currentText()
        self.data['proxy'] = self.enter_proxy_combo.currentText()
        self.itemEdit.emit(self.data)
        self.accept()

    def retranslateUi(self):
        # устанаваливает текст исходя из значений, переданных в self.data
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_taskBtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.header.setText(QCoreApplication.translate("Dialog", u"Edit Task #" + str(self.data['num']), None))
        self.exit_button.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.enter_site_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Svyaznoy", None))

        self.enter_site_label_4.setText(QCoreApplication.translate("Dialog", u"Site:", None))


        self.enter_profile_label_4.setText(QCoreApplication.translate("Dialog", u"Profile:", None))
        self.enter_product_label_4.setText(QCoreApplication.translate("Dialog", u"Product:", None))
        self.enter_size_combo.setItemText(0, QCoreApplication.translate("Dialog", u"No Size", None))

        self.enter_size_label_4.setText(QCoreApplication.translate("Dialog", u"Size:", None))
        self.enter_proxy_label_4.setText(QCoreApplication.translate("Dialog", u"Proxy:", None))

