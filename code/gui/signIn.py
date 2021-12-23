import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar, QLabel


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(1938, 1043)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("D:/CSED/Third Year/First Semester/SE/project/space/space/icons/icons8-space-64.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("QLineEdit{\n"
                           "background-color: rgba(230, 230, 230,0.6) ;\n"
                           "border: 5px solid rgba(0,0,0,0) ;\n"
                           "border-radius:4px ;\n"
                           "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                           "color: #14279B ;\n"
                           "padding-bottom:7px ;\n"
                           "}")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(240, 390, 281, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
                                 "background opacity: 0.0;")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 361, 91))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(250, 510, 251, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(570, 400, 401, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 2621, 1081))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-image:url(:/newPrefix/f.jpg);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-size: contain, cover;")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 510, 401, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStatusTip("")
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(50, 790, 81, 81))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:rgba(152,186,231,0.7);\n"
                                      "border-radius: 40px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#98BAE7;\n"
                                      "}\n"
                                      "")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/CSED/Third Year/First Semester/SE/project/space/space/icons/icons8-space"
                                      "-shuttle-50.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 510, 61, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
                                        "background:none;\n"
                                        "border: none;")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("D:/CSED/Third Year/First Semester/SE/project/space/space/icons/icons8-millenium-eye-64.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 800, 221, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("D:/CSED/Third Year/First Semester/SE/project/space/space/icons/icons8-space-32.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "User Name"))
        self.label_2.setText(_translate("Form", "Sign In"))
        self.label_3.setText(_translate("Form", "Password"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Your Password"))
        self.pushButton_3.setText(_translate("Form", "Let\'s GO"))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1579, 891)
        self.startUIWindow()
        self.movie = QMovie("f.JPG")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = UIWindow(self)
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
    w = MainWindow()
    sys.exit(app.exec_())
