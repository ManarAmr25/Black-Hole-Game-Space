'''import sys

from PyQt5.QtWidgets import QApplication

import signIn
import signUp
import gamespace
import start_page
from PyQt5 import QtCore,QtWidgets


def open_signin():
    signin = signIn.SigninMain()
    signin.Window.pushButton_3.clicked.connect(open_gamespace)
    widget.addWidget(signin)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def open_signup():
    signup = signUp.SignupMain()
    widget.addWidget(signup)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def open_gamespace():
    game = gamespace.GamespaceMain()
    widget.addWidget(game)
    widget.setCurrentIndex(widget.currentIndex() - 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    w = start_page.StartMain()
    w.Window.pushButton_2.clicked.connect(open_signin)
    w.Window.pushButton.clicked.connect(open_signup)
    w.Window.pushButton_3.clicked.connect(open_gamespace)
    widget.addWidget(w)
    widget.show()
    sys.exit(app.exec_())'''
from PyQt5.QtCore import QUrl, QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication
import sys

import signIn
import signUp
import gamespace
import start_page
import profile_page
import landing_page
from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

def signup_to_gamespace():
    if signup.Window.sign_up_db():
        open_gamespace()

def signin_to_gamespace():
    if signin.Window.sign_in_db():
        open_gamespace()

def open_startpage():
    widget.setCurrentIndex(0)

def open_signin():
    widget.setCurrentIndex(1)


def open_signup():
    widget.setCurrentIndex(2)


def open_gamespace():
    widget.setCurrentIndex(3)

def open_profile():
    widget.setCurrentIndex(4)

if __name__ == '__main__':
    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("../storage/Sounds/mixkit-alien-world-trailer-intro-2425.wav")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)
    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.play()
    app = QApplication(sys.argv)
    landing = landing_page.LandingMain()
    widget = QtWidgets.QStackedWidget()
    w = start_page.StartMain()
    signin = signIn.SigninMain()
    signup = signUp.SignupMain()
    game = gamespace.GamespaceMain()
    profile = profile_page.ProfileMain()
    w.Window.pushButton_2.clicked.connect(open_signin)
    w.Window.pushButton.clicked.connect(open_signup)
    w.Window.pushButton_3.clicked.connect(open_gamespace)
    #sign in navigation btns
    signin.Window.pushButton_3.clicked.connect(signin_to_gamespace)
    signin.Window.pushButton.clicked.connect(open_startpage)
    # sign up navigation btns
    signup.Window.pushButton_2.clicked.connect(signup_to_gamespace)
    signup.Window.pushButton.clicked.connect(open_startpage)
    #gamespace navigation btns
    game.Window.pushButton.clicked.connect(open_profile)
    game.Window.pushButton_3.clicked.connect(open_startpage)
    #profile navigation btns
    profile.Window.pushButton_4.clicked.connect(open_gamespace)
    widget.addWidget(w)
    widget.addWidget(signin)
    widget.addWidget(signup)
    widget.addWidget(game)
    widget.addWidget(profile)
    loop = QEventLoop()
    QTimer.singleShot(1000, loop.quit)
    loop.exec_()
    player.stop()
    del landing
    widget.show()
    sys.exit(app.exec_())