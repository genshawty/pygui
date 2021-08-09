from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from mainWindow import Ui_MainWindow

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        self.width = 862
        self.height = 660
        Form.resize(self.width, self.height)
        Form.move(centerPoint.x() - (self.width / 2), centerPoint.y() - (self.height / 2))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 50, 771, 591))
        self.left_back = QLabel(self.widget)
        self.left_back.setObjectName(u"left_back")
        self.left_back.setGeometry(QRect(90, 40, 351, 461))
        self.left_back.setStyleSheet(u"border: 1px solid white;")
        self.left_back.setPixmap(QPixmap(u"img/background-login.jpg"))
        self.left_back.setScaledContents(True)
        self.right_back = QLabel(self.widget)
        self.right_back.setObjectName(u"right_back")
        self.right_back.setGeometry(QRect(410, 50, 321, 441))
        font = QFont()
        font.setPointSize(20)
        self.right_back.setFont(font)
        self.right_back.setStyleSheet(u"background-color: rgb(255, 204, 153);\n"
"border: 2px solid transparent;\n"
"border-radius: 14px;\n"
"")
        self.enter_your_label = QLabel(self.widget)
        self.enter_your_label.setObjectName(u"enter_your_label")
        self.enter_your_label.setGeometry(QRect(460, 160, 251, 81))
    
        font1 = QFont()
        font1.setFamilies([u"Alef"])
        font1.setPointSize(17)
        font1.setItalic(False)
        self.enter_your_label.setFont(font1)
        self.enter_your_label.setAlignment(Qt.AlignCenter)
        self.input_key = QLineEdit(self.widget)
        self.input_key.setObjectName(u"input_key")
        self.input_key.setGeometry(QRect(460, 240, 251, 21))
        font2 = QFont()
        font2.setFamilies([u"Alef"])
        font2.setPointSize(11)
        self.input_key.setFont(font2)
        self.input_key.setMouseTracking(True)
        self.input_key.setFocusPolicy(Qt.ClickFocus)
        self.input_key.setStyleSheet(u"background-color: transparent;\n"
"border: 2px solid black;\n"
"border-radius: 3px;\n"
"color: rgb(59, 59, 59);")
        self.input_key.setFrame(False)
        self.input_key.setAlignment(Qt.AlignCenter)
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(460, 300, 251, 61))
        font3 = QFont()
        font3.setPointSize(15)
        self.loginButton.setFont(font3)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet(u"QPushButton#loginButton {\n"
"	background-color: rgb(254, 255, 241);\n"
"	\n"
"	\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#loginButton:hover {\n"
"	background-color: rgb(255, 220, 185);\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.exit_button = QPushButton(self.widget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(694, 60, 21, 24))
        self.exit_button.setStyleSheet(u"QPushButton#exit_button {\n"
"	border: 1px solid transparent;\n"
"	background-color: rgb(255, 204, 153);\n"
"}\n"
"QPushButton#exit_button:hover {\n"
"	background-color: rgba(255, 0, 0, 0.3);\n"
"}")

        self.response_text = QLabel(self.widget)
        self.response_text.setObjectName(u"response_text")
        self.response_text.setGeometry(QRect(460, 370, 251, 20))
        font4 = QFont()
        font4.setFamilies([u"Alef"])
        font4.setPointSize(11)
        self.response_text.setFont(font4)
        self.response_text.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.response_text.setAlignment(Qt.AlignCenter)

        self.exit_button.clicked.connect(lambda: Form.close())
        self.right_back.raise_()
        self.left_back.raise_()
        self.enter_your_label.raise_()
        self.input_key.raise_()
        self.loginButton.raise_()
        self.loginButton.clicked.connect(self.check_status)
        self.exit_button.raise_()
        self.response_text.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def check_status(self):
        print(self.input_key.text())
        self.main_window()

    def main_window(self):
        r = 1
        if r:
            self.response_text.setStyleSheet(u"color: rgb(0, 170, 0);")
            self.response_text.setText(QCoreApplication.translate("Form", u"Logged succsefully", None))
        else:
            self.response_text.setStyleSheet(u"color: rgb(0, 200, 0);")
            self.response_text.setText(QCoreApplication.translate("Form", u"access denied", None))
        
        # Create the Qt Application
        self.main_form = QMainWindow()
        # Create and show the form
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self.main_form)
        self.main_form.show()
        Form.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.left_back.setText("")
        self.right_back.setText("")
        self.enter_your_label.setText(QCoreApplication.translate("Form", u"Enter your license key:", None))
        # self.response_text.setText(QCoreApplication.translate("Form", u"", None))
        self.input_key.setPlaceholderText(QCoreApplication.translate("Form", u"license key", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    Form = QWidget()
    # Create and show the form
    login = Ui_Form()
    login.setupUi(Form)
    Form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
