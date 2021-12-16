import sys
import time

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar, QLabel

class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.resize(QSize(720, 1000))
        self.progressBar =QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(230, 850, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(95)
        font.setStrikeOut(False)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar\n")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setStyleSheet("QProgressBar\n"
                                       "{\n"
                                       "    background:rgba(255, 255, 255,0.5);\n"
                                       "    border-radius : 15px;\n"
                                       "text-align: center;\n"
                                       
                                       "\n"
                                       "}\n"
                                       "QProgressBar::chunk \n"
                                       "{\n"
                                       "background:rgb(110, 60,188,0.5);\n"
                                       
                                       "border-radius :15px;\n"
                                       "border:3px solid;\n"
                                       
                                       "border-color:    rgba(255, 255, 255,0.5);\n"
                                       "} ")

        self.lb = QLabel(self)
        self.lb.setText('Hello User :)')
        self.lb.setStyleSheet("border-radius:15px;\n"
                              "background:rgba(255, 255, 255,0.2);\n")
        self.lb.setAlignment(QtCore.Qt.AlignCenter)
        self.lb.setGeometry(QtCore.QRect(230, 900, 261, 30))
        self.lb.setFont(font)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(720, 1000)
        self.startUIWindow()
        self.movie = QMovie("giphy2.gif")
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
    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("mixkit-alien-world-trailer-intro-2425.wav")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)
    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.play()
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())