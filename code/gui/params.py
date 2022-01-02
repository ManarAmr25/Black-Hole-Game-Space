import sys
import time
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar, QLabel, QLineEdit

'''
old gamespace variables
label3: name
label4: level
label2: avatar
label5
label6 game
pushbutton go to profile
push3 exit

'''
'''
old start page variables
push2 sign in
push sign up
push 3 guest
label 2 title
label


'''


def init_font_landing():
    font = QtGui.QFont()
    font.setFamily("Papyrus")
    font.setPointSize(15)
    font.setBold(True)
    font.setWeight(95)
    font.setStrikeOut(False)
    return font


def init_font_start(size, isItalic):
    font = QtGui.QFont()
    font.setFamily("OCR A Extended")
    font.setPointSize(size)
    font.setBold(True)
    font.setItalic(isItalic)
    font.setWeight(75)
    return font


def get_font(size):
    font = QtGui.QFont()
    font.setFamily("OCR A Extended")
    font.setPointSize(size)
    return font


sign_in_lineEdit_style = "QLineEdit{\nbackground-color: rgba(230, 230, 230,0.6) ;\nborder: 5px solid rgba(0,0,0," \
                         "0) ;\nborder-radius:4px ;\nborder-bottom-color:rgba(46,82,101,200) ;\ncolor: #14279B " \
                         ";\npadding-bottom:7px ;\n} "

background_style = "background-image:url(:/newPrefix/f.jpg);\nbackground-repeat: no-repeat;\nbackground-size: " \
                   "contain, cover; "

back_button_style = "QPushButton{\nbackground-color:rgba(152,186,231,0.7);\nborder-radius: " \
                    "40px;\n}\nQPushButton:hover{\nbackground-color:#98BAE7;\n}\n "

show_password_button_style = "background-color: transparent;\nbackground:none;\nborder: none;"

next_button_style = "QPushButton {\nbackground:linear-gradient(to bottom, #599bb3 5%, #408c99 " \
                    "100%);\nbackground-color:#E6E6E6;\nborder-radius:8px;\nborder:1px solid " \
                    "#d6bcd6;\ncolor:#3a8a9e;\ntext-decoration:none;\ntext-shadow:0px 1px 0px " \
                    "#e1e2ed;\n}\nQPushButton:hover {\nbackground:linear-gradient(to bottom, #bab1ba 5%, " \
                    "#ededed 100%);\nbackground-color:#bab1ba;\n}\nQPushButton:active {" \
                    "\nposition:relative;\ntop:1px;\n} "

invalid_style = "QLabel{\ncolor:rgb(255,69,72);\n}"

# sizes
# land page

landing_width = 720
landing_height = 1000
land_page_progressbar_size = QRect(230, 850, 261, 30)

# gamespace
gamespace_width = 1920
gamespace_height = 1080

# backgrounds
landing_bcg = "../storage/BackGround/landing_page.gif"
gamespace_bcg = "../storage/BackGround/gamespace.jpg"
start_bcg = "../storage/BackGround/start.jpg"
# fonts
font_landing = init_font_landing()

# style sheets
progressbar_landing_sheet = ("QProgressBar\n"
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
quote_sheet = ("border-radius:15px;\n"
               "background:rgba(255, 255, 255,0.2);\n")
level_progress_sheet = ("QProgressBar:horizontal {\n"
                        "border: 1px solid gray;\n"
                        "border-radius: 3px;\n"
                        "background: white;\n"
                        "padding: 3px;\n"
                        "text-align: center;\n"
                        "margin-right: 4ex;\n"
                        "}\n"
                        "QProgressBar::chunk:horizontal {\n"
                        "background:rgb(241, 236, 83);\n"
                        "width: 10px;\n"
                        "\n"
                        "}")
startpg_buttons_sheet = ("QPushButton{\n"
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
landing_title = "Black Hole"
gamespace_title = "Home"
startpage_title = "Welcome Alien"
