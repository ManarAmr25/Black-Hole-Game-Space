
from PyQt5.QtCore import QUrl, QEventLoop, QTimer, QElapsedTimer
from PyQt5.QtWidgets import QApplication
import sys
import signIn
import signUp
import gamespace
import start_page
import profile_page
import landing_page
import leaderboard
from PyQt5 import QtWidgets, QtTest
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

def signup_to_gamespace():
    if signup.Window.sign_up_db():
        open_gamespace()

def signin_to_gamespace():
    if signin.Window.sign_in_db():
        open_gamespace()

def open_startpage():
    widget.setCurrentIndex(0)
    w.refresh()

def open_signin():
    widget.setCurrentIndex(1)
    signin.refresh()


def open_signup():
    widget.setCurrentIndex(2)
    signup.refresh()


def open_gamespace():
    widget.setCurrentIndex(3)
    game.refresh()


def open_profile():
    widget.setCurrentIndex(4)
    profile.refresh()


def open_leaderboard():
    widget.setCurrentIndex(5)
    leaderboard.refresh()


if __name__ == '__main__':
    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("../storage/Sounds/mixkit-alien-world-trailer-intro-2425.wav")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)
    player = QMediaPlayer()
    player.setPlaylist(playlist)
    # player.play()
    app = QApplication(sys.argv)
    landing = landing_page.LandingMain()
    #start widget
    widget = QtWidgets.QStackedWidget()
    w = start_page.StartMain()
    signin = signIn.SigninMain()
    signup = signUp.SignupMain()
    game = gamespace.GamespaceMain()
    profile = profile_page.ProfileMain()
    leaderboard = leaderboard.LeaderboardMain()
    w.Window.signin_btn.clicked.connect(open_signin)
    w.Window.signup_btn.clicked.connect(open_signup)
    w.Window.guest_btn.clicked.connect(open_gamespace)
    w.Window.quit_btn.clicked.connect(sys.exit)
    #sign in navigation btns
    signin.Window.next_button.clicked.connect(signin_to_gamespace)
    signin.Window.back_button.clicked.connect(open_startpage)
    # sign up navigation btns
    signup.Window.next_button.clicked.connect(signup_to_gamespace)
    signup.Window.back_button.clicked.connect(open_startpage)
    #gamespace navigation btns
    game.Window.profilebtn.clicked.connect(open_profile)
    game.Window.exitbtn.clicked.connect(open_startpage)
    game.Window.leaderboardbtn.clicked.connect(open_leaderboard)
    #profile navigation btns
    profile.Window.back_button.clicked.connect(open_gamespace)
    #leaderboard navigation
    leaderboard.Window.back_button.clicked.connect(open_gamespace)

    widget.addWidget(w)  # 0
    widget.addWidget(signin)  # 1
    widget.addWidget(signup)  # 2
    widget.addWidget(game)  # 3
    widget.addWidget(profile)  # 4
    widget.addWidget(leaderboard)  # 5

    loop = QEventLoop()
    t = QElapsedTimer()
    for i in range(6):
        landing.Window.progressBar.setValue(i*20)
        QtTest.QTest.qWait(400)

    QTimer.singleShot(500, loop.quit)
    loop.exec_()

    # player.stop()
    del landing
    # widget.showFullScreen()
    widget.show()
    widget.move(10,10)
    # widget.update()
    sys.exit(app.exec_())