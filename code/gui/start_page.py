import sys
from signIn import SigninMain
from signUp import SignupMain
from gamespace import GamespaceMain
from PyQt5 import QtCore,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class StartWindow(QWidget):
    def open_signin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=SigninMain()
        w.hide()

    def open_signup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SignupMain()
        w.hide()

    def open_gamespace(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=GamespaceMain()
        w.hide()

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(1579, 891)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet("QPushButton{\n"
                           "    box-shadow: -1px 0px 6px 0px #F0D9FF;\n"
                           "    background-color:#6E3CBC;\n"
                           "    border-radius:38px;\n"
                           "    border:4px solid #F0D9FF;\n"
                           "    cursor:pointer;\n"
                           "    color:#ffffff;\n"
                           "    font-size:26px;\n"
                           "    font-family:OCR A Extended;\n"
                           "    font-style:italic;\n"
                           "    font-weight:bold;\n"
                           "    padding:22px 15px;\n"
                           "}\n"
                           "QPushButton:hover {\n"
                           "    background-color:#BFA2DB;\n"
                           "}")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(-19, -9, 1600, 1200))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 280, 421, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        #TODO actions
        self.pushButton_2.clicked.connect(self.open_signin)
        self.pushButton.clicked.connect(self.open_signup)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_gamespace)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(650, 170, 591, 111))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(51)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(213, 221, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BLACK HoLE"))
        self.pushButton_2.setText(_translate("Form", "Sign In"))
        self.pushButton.setText(_translate("Form", "Sign Up"))
        self.pushButton_3.setText(_translate("Form", "Play as a guest"))
        self.label_2.setText(_translate("Form", "BLACK HoLE"))


class StartMain(QMainWindow):
    def __init__(self, parent=None):
        super(StartMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/start.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = StartWindow(self)
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
    w = StartMain()
    sys.exit(app.exec_())
