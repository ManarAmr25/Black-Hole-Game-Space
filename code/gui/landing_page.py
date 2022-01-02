from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QProgressBar, QLabel
from params import *


class LandingWindow(QWidget):

    def init_progressbar(self):
        progressbar = QProgressBar(self)
        progressbar.setGeometry(land_page_progressbar_size)
        progressbar.setFont(font_landing)
        progressbar.setStyleSheet("QProgressBar\n")
        progressbar.setProperty("value", 24)
        progressbar.setStyleSheet(progressbar_landing_sheet)
        return progressbar

    def init_quote_lb(self):
        lb = QLabel(self)
        # TODO get random quote
        lb.setText('Hello User :)')
        lb.setStyleSheet(quote_sheet)
        lb.setAlignment(QtCore.Qt.AlignCenter)
        lb.setGeometry(QtCore.QRect(230, 900, 261, 30))
        lb.setFont(font_landing)
        return lb

    def __init__(self, parent=None):
        super(LandingWindow, self).__init__(parent)
        # resize window
        self.resize(QSize(landing_width, landing_height))
        # loading progressbar
        self.progressBar = self.init_progressbar()
        # quote label
        self.quote = self.init_quote_lb()


class LandingMain(QMainWindow):
    def __init__(self, parent=None):
        super(LandingMain, self).__init__(parent)
        # position of window
        self.setGeometry(600, 35, 600, 750)
        # size of window
        self.setFixedSize(landing_width, landing_height)
        self.startUIWindow()
        # background
        self.movie = QMovie(landing_bcg)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = LandingWindow(self)
        self.setWindowTitle(landing_title)
        self.show()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
