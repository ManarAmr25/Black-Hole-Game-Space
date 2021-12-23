import sys
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar, QLabel


class SignupWindow(QWidget):
    def __init__(self, parent=None):
        super(SignupWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(1383, 858)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setFont(font)
        self.setStyleSheet("")
        self.userNameLbl = QtWidgets.QLabel(self)
        self.userNameLbl.setGeometry(QtCore.QRect(240, 390, 291, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.userNameLbl.setFont(font)
        self.userNameLbl.setStyleSheet("color: white;\n"
                                       "background opacity: 0.0;")
        self.userNameLbl.setScaledContents(False)
        self.userNameLbl.setObjectName("userNameLbl")
        self.signUpLbl = QtWidgets.QLabel(self)
        self.signUpLbl.setGeometry(QtCore.QRect(80, 130, 381, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(50)
        self.signUpLbl.setFont(font)
        self.signUpLbl.setStyleSheet("color: white;")
        self.signUpLbl.setScaledContents(False)
        self.signUpLbl.setObjectName("signUpLbl")
        self.passwordLbl = QtWidgets.QLabel(self)
        self.passwordLbl.setGeometry(QtCore.QRect(250, 510, 271, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.passwordLbl.setFont(font)
        self.passwordLbl.setStyleSheet("color: white;")
        self.passwordLbl.setScaledContents(False)
        self.passwordLbl.setObjectName("passwordLbl")
        self.userNameTxtBox = QtWidgets.QLineEdit(self)
        self.userNameTxtBox.setGeometry(QtCore.QRect(570, 390, 401, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.userNameTxtBox.setFont(font)
        self.userNameTxtBox.setStyleSheet("background-color: rgba(230, 230, 230,0.6) ;\n"
                                          "border: 5px solid rgba(0,0,0,0) ;\n"
                                          "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                                          "color: #14279B ;\n"
                                          "padding-bottom:7px ;\n"
                                          "\n"
                                          "")
        self.userNameTxtBox.setText("")
        self.userNameTxtBox.setObjectName("userNameTxtBox")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(0, -30, 2591, 1081))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(32)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background-image:url(C:/Users/EMAN MOHAMED/Desktop/Sign in/signUp.jpeg);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-size: contain, cover;")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.passwordTxtBox = QtWidgets.QLineEdit(self)
        self.passwordTxtBox.setGeometry(QtCore.QRect(570, 500, 401, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.passwordTxtBox.setFont(font)
        self.passwordTxtBox.setStyleSheet("background-color: rgba(230, 230, 230,0.6) ;\n"
                                          "border: 5px solid rgba(0,0,0,0) ;\n"
                                          "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                                          "color: #14279B ;\n"
                                          "padding-bottom:7px ;")
        self.passwordTxtBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordTxtBox.setObjectName("passwordTxtBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(50, 770, 80, 80))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:rgba(152,186,231,0.7);\n"
                                      "border:none;\n"
                                      "border-radius: 40px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(152,186,231)\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../storage/Icons/back.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.showPasswordBtn = QtWidgets.QPushButton(self)
        self.showPasswordBtn.setGeometry(QtCore.QRect(920, 500, 51, 51))
        self.showPasswordBtn.setStyleSheet("background-color:transparent;\n"
                                           "background:none;\n"
                                           "border:none;")
        self.showPasswordBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "../storage/Icons/showPassword.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showPasswordBtn.setIcon(icon1)
        self.showPasswordBtn.setIconSize(QtCore.QSize(80, 80))
        self.showPasswordBtn.setObjectName("showPasswordBtn")
        self.genderLbl = QtWidgets.QLabel(self)
        self.genderLbl.setGeometry(QtCore.QRect(270, 630, 191, 81))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.genderLbl.setFont(font)
        self.genderLbl.setStyleSheet("QLabel{\n"
                                     "color:white;\n"
                                     "}")
        self.genderLbl.setObjectName("genderLbl")
        self.maleRdBtn = QtWidgets.QRadioButton(self)
        self.maleRdBtn.setGeometry(QtCore.QRect(560, 650, 151, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.maleRdBtn.setFont(font)
        self.maleRdBtn.setStyleSheet("QRadioButton{\n"
                                     "color:rgb(248, 255, 105);\n"
                                     "\n"
                                     "}\n"
                                     "")
        self.maleRdBtn.setObjectName("maleRdBtn")
        self.femaleRdBtn = QtWidgets.QRadioButton(self)
        self.femaleRdBtn.setGeometry(QtCore.QRect(810, 650, 221, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.femaleRdBtn.setFont(font)
        self.femaleRdBtn.setStyleSheet("color:rgb(248, 255, 105);")
        self.femaleRdBtn.setObjectName("femaleRdBtn")
        self.invalidNameLbl = QtWidgets.QLabel(self)
        self.invalidNameLbl.setGeometry(QtCore.QRect(990, 390, 221, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.invalidNameLbl.setFont(font)
        self.invalidNameLbl.setStyleSheet("QLabel{\n"
                                          "color:rgb(255,69,72);\n"
                                          "}")
        self.invalidNameLbl.setObjectName("invalidNameLbl")
        self.changePasswordLbl = QtWidgets.QLabel(self)
        self.changePasswordLbl.setGeometry(QtCore.QRect(990, 510, 301, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.changePasswordLbl.setFont(font)
        self.changePasswordLbl.setStyleSheet("QLabel{\n"
                                             "color:rgb(255,69,72);\n"
                                             "}")
        self.changePasswordLbl.setObjectName("changePasswordLbl")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 800, 221, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
                                        "    background-color:#E6E6E6;\n"
                                        "    border-radius:8px;\n"
                                        "    border:1px solid #d6bcd6;\n"
                                        "    color:#3a8a9e;\n"
                                        "    text-decoration:none;\n"
                                        "    text-shadow:0px 1px 0px #e1e2ed;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background:linear-gradient(to bottom, #bab1ba 5%, #ededed 100%);\n"
                                        "    background-color:#bab1ba;\n"
                                        "}\n"
                                        "QPushButton:active {\n"
                                        "    position:relative;\n"
                                        "    top:1px;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "../storage/Icons/nextPage.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4.raise_()
        self.userNameLbl.raise_()
        self.signUpLbl.raise_()
        self.passwordLbl.raise_()
        self.userNameTxtBox.raise_()
        self.passwordTxtBox.raise_()
        self.pushButton.raise_()
        self.showPasswordBtn.raise_()
        self.genderLbl.raise_()
        self.maleRdBtn.raise_()
        self.femaleRdBtn.raise_()
        self.invalidNameLbl.raise_()
        self.changePasswordLbl.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userNameLbl.setText(_translate("Form", "User Name"))
        self.signUpLbl.setText(_translate("Form", "Sign Up"))
        self.passwordLbl.setText(_translate("Form", "Password"))
        self.userNameTxtBox.setPlaceholderText(_translate("Form", "Enter Your Name"))
        self.passwordTxtBox.setPlaceholderText(_translate("Form", "Enter Your Password"))
        self.genderLbl.setText(_translate("Form", "Gender"))
        self.maleRdBtn.setText(_translate("Form", "Male"))
        self.femaleRdBtn.setText(_translate("Form", "Female"))
        self.invalidNameLbl.setText(_translate("Form", "Invalid Name"))
        self.changePasswordLbl.setText(_translate("Form", "Invalid Password"))
        self.pushButton_2.setText(_translate("Form", "Let\'s Go"))



class SignupMain(QMainWindow):
    def __init__(self, parent=None):
        super(SignupMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/user.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = SignupWindow(self)
        self.setWindowTitle("My Program")
        self.show()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SignupMain()
    sys.exit(app.exec_())
