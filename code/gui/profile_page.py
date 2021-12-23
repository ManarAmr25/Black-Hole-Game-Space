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
        self.resize(1920, 1020)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.setFont(font)
        self.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-space-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(380, 40, 631, 81))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("border-left: 10px solid  rgb(255, 255, 255);\n"
                                 "background-color: rgba(184, 228, 240,0.3);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 251, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(251, 231))
        self.label_2.setStyleSheet("border-radius: 7px;\n"
                                   "background-color: rgba(0, 0, 49,0.6);\n"
                                   "border : 2px groove rgb(157, 158, 253);\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(5)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1920, 1050))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/WhatsApp Image 2021-12-14 at 10.00.04 PM.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(340, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-left: 5px solid  rgb(255, 255, 255);\n"
                                   "border-radius : 10px;\n"
                                   "")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 510, 291, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color:rgb(248, 255, 105);\n"
                                      "    font: 11pt \"OCR A Extended\";\n"
                                      "    border-radius: 1px;\n"
                                      "    border-bottom: 4px solid rgba(152, 186, 231,0);\n"
                                      "    font-weight: 500;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    color: rgb(9, 6, 75);\n"
                                      "    background-color: rgba(152, 186, 231,0.7);\n"
                                      "    border-bottom: 4px solid rgb(152, 186, 231);\n"
                                      "    font: 11pt \"OCR A Extended\";\n"
                                      "    box-sizing: border-box;\n"
                                      "    font-weight: 500;\n"
                                      "}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(340, 410, 201, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-left: 5px solid  rgb(255, 255, 255);\n"
                                   "border-radius : 10px;\n"
                                   "")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(620, 240, 341, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgba(230, 230, 230,0) ;\n"
                                    "    font: 20pt \"OCR A Extended\";\n"
                                    "    border-radius: 1px;\n"
                                    "    border-bottom: 5px solid rgba(255,255,255,0);\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "    background-color: rgba(230, 230, 230,0.6) ;\n"
                                    "    border-bottom: 5px solid rgba(255,255,255,1);\n"
                                    "}\n"
                                    "")
        self.lineEdit.setInputMask("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 250, 71, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    color:rgb(248, 255, 105);\n"
                                        "    font: 11pt \"OCR A Extended\";\n"
                                        "    border-radius: 1px;\n"
                                        "    border-bottom: 4px solid rgba(152, 186, 231,0);\n"
                                        "    font-weight: 500;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(9, 18, 97);\n"
                                        "    background-color: rgba(152, 186, 231,0.7);\n"
                                        "    border-bottom: 4px solid rgb(152, 186, 231);\n"
                                        "    font: 11pt \"OCR A Extended\";\n"
                                        "    box-sizing: border-box;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(1130, 250, 260, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(62)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 69, 72);\n"
                                   "font-weight: 500;\n"
                                   "font-size: 10pt;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 340, 191, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    color:rgb(248, 255, 105);\n"
                                        "    font: 11pt \"OCR A Extended\";\n"
                                        "    border-radius: 1px;\n"
                                        "    border-bottom: 4px solid rgba(152, 186, 231,0);\n"
                                        "    font-weight: 500;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(9, 6, 75);\n"
                                        "    background-color: rgba(152, 186, 231,0.7);\n"
                                        "    border-bottom: 4px solid rgb(152, 186, 231);\n"
                                        "    font: 11pt \"OCR A Extended\";\n"
                                        "    box-sizing: border-box;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(440, 480, 721, 341))
        self.frame.setStyleSheet("border-left : 7px solid rgb(255, 255, 255);\n"
                                 "background-color : rgba(184, 228, 240,0.3); ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border : none;")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 910, 80, 80))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    border-radius : 40px;\n"
                                        "    background-color: rgba(152, 186, 231,0.7);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(152, 186, 231);\n"
                                        "}")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../space/icons/icons8-space-shuttle-50.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.pushButton_3.raise_()
        self.frame.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(self)
        self.pushButton_2.clicked.connect(self.lineEdit.showNormal)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "profile"))
        self.label.setText(_translate("Form", "Player\'s Profile"))
        self.label_2.setText(_translate("Form", "profile image"))
        self.label_5.setText(_translate("Form", "User Name:"))
        self.pushButton.setText(_translate("Form", "Change Profile Picture"))
        self.label_7.setText(_translate("Form", "Stats:"))
        self.lineEdit.setText(_translate("Form", "Player\'s name"))
        self.pushButton_2.setText(_translate("Form", "Edit"))
        self.label_6.setText(_translate("Form", "User Name already exists"))
        self.pushButton_3.setText(_translate("Form", "Change password"))
        self.label_8.setText(_translate("Form", " number of wins : "))


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
