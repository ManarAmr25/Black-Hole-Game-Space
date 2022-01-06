<<<<<<< HEAD
import numpy as np
import winsound
from PyQt5 import QtTest
from games.connect4 import pruning
from games.connect4.heuristic import *
from PyQt5.QtGui import QImage
import pygame
from gui.params import *
=======
import time
import numpy as np
import winsound
from PyQt5 import QtCore, QtTest
from games.connect4 import pruning, minimax
from games.connect4.heuristic import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
import pygame
import sys


class ImageWidget(QWidget, QtCore.QObject):
    def __init__(self, surface, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.data = surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)
        self.surface =surface
        self.setMouseTracking(True)
        self.loop = True
        self.xpos =0
        self.ypos =0;
    def mouseMoveEvent(self, event):
        self.loop = True
        self.xpos = event.x()
        self.ypos =event.y()

    def mousePressEvent(self, event):
        self.loop = False

    def update(self, surface):
        self.data = surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)
        self.paintEvent(event=[])


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.surface = surface
        self.img = ImageWidget(self.surface)
        self.setCentralWidget(self.img)
    def upd(self):
        global screen
        self.img.update(screen)
>>>>>>> 39c399676760fc43fa754274862b0bd97d6bd254

# TODO need to be in class
# size of circle and dimensions of board
SQUARESIZE = 150
ROWS = 6
COLUMNS = 7
<<<<<<< HEAD
=======
K = 3 #max depth
P = 0 #pruning option
>>>>>>> 39c399676760fc43fa754274862b0bd97d6bd254
RADIUS = SQUARESIZE // 2 - 5
# Colors
COLOR = [(237, 237, 237), (255, 204, 92), (255, 111, 105)]  # circle's colors
BOARD_COLOR = (88, 140, 126)

# screen size and dimensions
width = (COLUMNS + 10) * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)

# initialize BOARD
board = np.zeros((ROWS, COLUMNS), dtype=int)
screen = pygame.Surface((width, height))


class ImageWidget(QWidget, QtCore.QObject):
    global screen , board
    def __init__(self, surface, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.data = surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)
        self.surface = surface
        self.setMouseTracking(True)
        self.loop = True
        self.xpos = 0
        self.ypos = 0

    def mouseMoveEvent(self, event):
        self.loop = True
        self.xpos = event.x()
        self.ypos = event.y()

    def mousePressEvent(self, event):
        self.loop = False

    def update(self, surface):
        self.data = surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)
        self.paintEvent(event=[])

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    global screen, board
    def init_score_table(self):
        score_table = QtWidgets.QTableWidget(self.centralWidget())
        score_table.setGeometry(QtCore.QRect(1380, 220, 500, 200))
        score_table.setFixedHeight(570)
        score_table.horizontalScrollBar().hide()
        score_table.setStyleSheet(achievment_table_style)
        score_table.verticalScrollBar().setStyleSheet(scroll_style)
        score_table.setObjectName("scores_table")
        score_table.setFont(init_font_start(25, False))
        score_table.horizontalHeader().setFont(init_font_start(10, False))
        score_table.setColumnCount(2)
        score_table.setColumnWidth(0, 250)
        score_table.setColumnWidth(1, 250)
        score_table.setRowCount(1)
        score_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        score_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        score_table.verticalHeader().hide()
        # score_table.setShowGrid(False)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Player 1")
        score_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Player 2")
        score_table.setHorizontalHeaderItem(1, item)
        score_table.resetVerticalScrollMode()
        score_table.setSortingEnabled(False)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(str(0))
        score_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(str(0))
        score_table.setItem(0, 1, item)
        score_table.setRowHeight(0, 100)
        return score_table

    def setScores(self, s1, s2):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(str(s1))
        self.scores_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(str(s2))
        self.scores_table.setItem(0, 1, item)

    def get_label(self, background, offset):
        circlelbl = QtWidgets.QLabel(self.centralWidget())
        circlelbl.setGeometry(QtCore.QRect(1450 + offset, 80, 100, 100))
        circlelbl.setStyleSheet(f"background-color:{background};\n"
                                "border-radius:50px;")
        circlelbl.setObjectName("circlelbl")
        return circlelbl

    def get_winnerlbl(self):
        winnerlbl = QLabel("PLAYER 1 WINS !", self.centralWidget())
        # setting geometry of label
        winnerlbl.setGeometry(1380, 700, 400, 50)
        # setting border to the label
        winnerlbl.setStyleSheet("color: red; background-color: rgba(88, 140, 126,0.3)")
        # setting font to the label
        winnerlbl.setFont(init_font_start(20, False))
        # setting alignment ot the label
        winnerlbl.setAlignment(Qt.AlignCenter)
        winnerlbl.hide()
        return winnerlbl

    def init_quitbtn(self):
        quit_btn = QtWidgets.QPushButton(self.centralWidget())
        quit_btn.setGeometry(QtCore.QRect(1580, 890, 81, 81))
        quit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        quit_btn.setStyleSheet("QPushButton{\n"
                               "background-color:rgba(88, 140, 126,0.7);\n"
                               "border-radius: 40px;\n"
                               "}\n"
                               "QPushButton:hover{\n"
                               "background-color:#98BAE7;\n"
                               "}\n"
                               "")
        quit_btn.setText("Quit")
        quit_btn.setObjectName("quitbtn")
        return quit_btn

    def __init__(self, parent=None):
        global screen
        for r in range(ROWS):
            for j in range(7,17):
                pygame.draw.rect(screen, COLOR[0], (j * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))

        super(MainWindow, self).__init__(parent)
        # game variables
        self.K = 3
        self.mode = 0
        self.player = None
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.surface = screen
        self.img = ImageWidget(self.surface)
        self.setCentralWidget(self.img)
        self.centralWidget().setGeometry(QtCore.QRect(20, 20, 1000, 1000))
        self.scores_table = self.init_score_table()
        self.player1_color = self.get_label("rgb(255, 204, 92)", 0)
        self.player2_color = self.get_label("rgb(255, 111, 105)", 250)
        self.start = True
        # creating label to show the seconds
        self.timelbl = QLabel("00:00", self.centralWidget())

        # setting geometry of label
        self.timelbl.setGeometry(1520, 500, 200, 50)

        # setting border to the label
        self.timelbl.setStyleSheet("border : 3px solid black")

        # setting font to the label
        self.timelbl.setFont(init_font_landing())

        # setting alignment ot the label
        self.timelbl.setAlignment(Qt.AlignCenter)

        # title
        self.lbl = QLabel("TIME", self.centralWidget())

<<<<<<< HEAD
        # setting geometry of label
        self.lbl.setGeometry(1520, 430, 200, 50)

        # setting border to the label
        # self.lbl.setStyleSheet("border : 3px solid black")

        # setting font to the label
        self.lbl.setFont(init_font_start(20, False))

        # setting alignment ot the label
        self.lbl.setAlignment(Qt.AlignCenter)

        self.count = 0
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every  second
        timer.start(1000)

        # label to declare winner
        self.winnerlbl = self.get_winnerlbl()
        self.quitbtn = self.init_quitbtn()

    def set_player(self, player):
        self.player = player

    def showTime(self):
        # checking if flag is true
        if self.start:
            # getting text from count
            minutes = self.count // 60
            seconds = self.count % 60
            minutestxt = str(minutes) if minutes > 9 else ("0" + str(minutes))
            secondstxt = str(seconds) if seconds > 9 else ("0" + str(seconds))
            text = minutestxt + " : " + secondstxt
            self.count += 1
            # showing text
            self.timelbl.setText(text)

    def upd(self):
        global screen
        self.img.update(screen)

    # displays a circle in the game window
    def draw_circle(self, r, c, color):
        pygame.draw.circle(screen, color, (int((c + 0.5) * SQUARESIZE), int((r + 1.5) * SQUARESIZE)), RADIUS)

    # displays a rectangle in the game window
    def draw_rect(self, r, c):
        pygame.draw.rect(screen, BOARD_COLOR, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))

    # displays game board
    def draw_board(self, board):
        board = np.flip(board, 0)
        for r in range(ROWS):
            pygame.draw.rect(screen, COLOR[0], (0 * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
        for r in range(ROWS):
            for c in range(COLUMNS):
                self.draw_rect(r, c + 1)
                self.draw_circle(r, c + 1, COLOR[board[r][c]])

    # places a piece in the board array for the current turn
    def put_piece(self, board, last_in_row, c, turn):
        row = last_in_row[c]
        if row == ROWS:  # move not valid
            return False
        # update the last empty row in column c
        last_in_row[c] += 1
        # put the piece
        board[row][c] = turn
        return True

    # update scores
    def update_score(self, board, turn):
        ROWS = len(board)
        COLUMNS = len(board[0])
        score = 0
        for r in range(ROWS):
            for c in range(COLUMNS - 3):
                if board[r][c] == turn and board[r][c] == board[r][c + 1] and board[r][c + 1] == board[r][c + 2] and \
                        board[r][c + 2] == board[r][c + 3]:
                    score += 1

        # check COLUMNS
        for r in range(ROWS - 3):
            for c in range(COLUMNS):
                if board[r][c] == turn and board[r][c] == board[r + 1][c] and board[r + 1][c] == board[r + 2][c] and \
                        board[r + 2][c] == board[r + 3][c]:
                    score += 1

        # check +ve diagonals
        for r in range(ROWS - 3):
            for c in range(COLUMNS - 3):
                if board[r][c] == turn and board[r][c] == board[r + 1][c + 1] and board[r + 1][c + 1] == board[r + 2][
                    c + 2] and board[r + 2][c + 2] == board[r + 3][c + 3]:
                    score += 1

        # check -ve diagonals
        for r in range(3, ROWS):
            for c in range(COLUMNS - 3):
                if board[r][c] == turn and board[r][c] == board[r - 1][c + 1] and board[r - 1][c + 1] == board[r - 2][
                    c + 2] and board[r - 2][c + 2] == board[r - 3][c + 3]:
                    score += 1

        return score

    def game(self):
        global screen, board
        pygame.init()
        pygame.draw.rect(screen, COLOR[0], (0, 0, width, SQUARESIZE))
        self.count = 0
        self.start = True
        self.winnerlbl.setStyleSheet("color: black; background-color: rgba(88, 140, 126,0.3)")
        self.winnerlbl.setText("PLAYER 1 WINS !")
        self.winnerlbl.hide()
        print(self.mode)
        board = np.zeros((ROWS, COLUMNS), dtype=int)
        # put_piece(board, last_in_row, 3, 1)
        self.draw_board(board)
        self.upd()
        game_over = False
        self.scores = [0, 0]  # scores[0] > computer, scores[1] > human
        # keep track of last row in each col
        self.last_in_row = np.zeros(COLUMNS, dtype=int)
        self.turn = 0  # computer always goes first
        while not game_over:
            if check_end(self.last_in_row):  # check game end
                game_over = True
                print("End")
                self.start = False
                color = ["green", "rgb(255, 204, 92)"]
                self.winnerlbl.show()
                if self.scores[0] == self.scores[1]:
                    self.winnerlbl.setText("TIE")
                else:
                    if self.mode == 0:  # player vs computer
                        self.player.increment_games()
                        gained = 5 + max((self.scores[1] - self.scores[0])*2, 0)
                        print("in connect 4", self.scores, gained)
                        self.player.increase_xp(gained)
                        self.player.increase_weekly_xp(gained)
                    if self.scores[0] < self.scores[1]:
                        self.winnerlbl.setText("PLAYER 2 WINS !")
                        color[1] = "rgb(255, 111, 105)"
                        if self.mode == 0:
                            self.player.increment_wins()
                    for i in range(10):
                        self.winnerlbl.setStyleSheet(
                            f"color: {color[i % 2]}; background-color: rgba(88, 140, 126,0.3);")
                        self.upd()
                        self.repaint()
                        QtTest.QTest.qWait(200)
                self.player.update_achievements("game")
                self.player.update_achievements("xp")
                self.player.update_achievements("wins")
                self.player.update_achievements("level")
                # TODO : daily challenges

            elif self.turn == 0:  # computer's turn
                if self.mode ==0 :
                    self.computer_play()
                else:
                    self.human_play()
            else:
                self.human_play()

    def computer_play(self):
        best_move = pruning.decision(board, self.last_in_row, self.K)
        self.put_piece(board, self.last_in_row, best_move, self.turn + 1)
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        self.draw_board(board)
        self.scores[self.turn] = self.update_score(board, self.turn + 1)
        self.setScores(self.scores[0], self.scores[1])
        self.upd()
        self.turn = (self.turn + 1) % 2
        self.img.setMouseTracking(True)
        self.img.loop = True
    def human_play(self):
        self.img.loop = True
        while self.img.loop:
            pygame.draw.rect(screen, COLOR[0], (0, 0, width, SQUARESIZE))
            posx = self.img.xpos - 1 * SQUARESIZE
            col = posx // SQUARESIZE
            if posx > 0 and col < 7:
                self.draw_circle(-1, col + 1, COLOR[self.turn + 1])
                self.upd()
                self.repaint()
            QtTest.QTest.qWait(100)
            if not self.img.loop:
                break
        # human plays
        posx = self.img.xpos - 1 * SQUARESIZE
        col = posx // SQUARESIZE
        if posx > 0 and col < 7:
            if not self.put_piece(board, self.last_in_row, col, self.turn + 1):
                self.img.loop = True
                return
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            self.draw_board(board)
            self.scores[self.turn] = self.update_score(board, self.turn + 1)
            self.setScores(self.scores[0], self.scores[1])
            self.upd()
            self.repaint()
            self.turn = (self.turn + 1) % 2
        else:
            self.img.loop = True

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showFullScreen()
    w.game()
    sys.exit(app.exec_())
'''
=======
#displays a circle in the game window
def draw_circle(r, c, color):
    pygame.draw.circle(screen, color, (int((c + 0.5) * SQUARESIZE), int((r + 1.5) * SQUARESIZE)), RADIUS)

#displays a rectangle in the game window
def draw_rect(r, c):
    pygame.draw.rect(screen, BOARD_COLOR, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))

#displays game board
def draw_board(board):
    pygame.draw.rect(screen, COLOR[0], (0, 0, width, SQUARESIZE))
    board = np.flip(board, 0)
    for r in range(ROWS):
        for c in range(COLUMNS):
            draw_rect(r, c)
            draw_circle(r, c, COLOR[board[r][c]])


#places a piece in the board array for the current turn
def put_piece(board, last_in_row, c, turn):
    row = last_in_row[c]
    if row == ROWS: #move not valid
        return False
    # update the last empty row in column c
    last_in_row[c] += 1
    # put the piece
    board[row][c] = turn
    return True


# update scores
def update_score(board, turn):
    ROWS = len(board)
    COLUMNS = len(board[0])
    score = 0
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == turn and board[r][c] == board[r][c + 1] and board[r][c + 1] == board[r][c + 2] and \
                    board[r][c + 2] == board[r][c + 3]:
                score += 1

    # check COLUMNS
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if board[r][c] == turn and board[r][c] == board[r + 1][c] and board[r + 1][c] == board[r + 2][c] and \
                    board[r + 2][c] == board[r + 3][c]:
                score += 1

    # check +ve diagonals
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if board[r][c] == turn and board[r][c] == board[r + 1][c + 1] and board[r + 1][c + 1] == board[r + 2][
                c + 2] and board[r + 2][c + 2] == board[r + 3][c + 3]:
                score += 1

    #check -ve diagonals
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == turn and board[r][c] == board[r - 1][c + 1] and board[r - 1][c + 1] == board[r - 2][
                c + 2] and board[r - 2][c + 2] == board[r - 3][c + 3]:
                score += 1

    return score
screen =None
def start():
    if __name__ == '__main__':
        pygame.init()
        global  screen
        screen = pygame.Surface((width, height))
        game_over = False
        scores = [0, 0]  # scores[0] > computer, scores[1] > human
        # keep track of last row in each col
        last_in_row = np.zeros(COLUMNS, dtype=int)
        turn = 0  # computer always goes first
        #put_piece(board, last_in_row, 3, 1)
        draw_board(board)
        app = QApplication(sys.argv)
        w = MainWindow(screen)
        w.show()

        while not game_over:
            if check_end(last_in_row):  # check game end
                game_over = True
                print("End")
            elif turn == 0:  # computer's turn
                if P == 1:  # with pruning
                    start_time = time.time()
                    best_move = pruning.decision(board, last_in_row, K)
                    total_time = int((time.time() - start_time) * 1000)
                else:  # without pruning
                    start_time = time.time()
                    best_move = minimax.decision(board, last_in_row, K)
                    total_time = int((time.time() - start_time) * 1000)
                put_piece(board, last_in_row, best_move, turn + 1)
                winsound.PlaySound('mixkit-small-hit-in-a-game-2072.wav', winsound.SND_ASYNC)
                draw_board(board)
                w.upd()
                scores[turn] = update_score(board, turn + 1)
                turn = (turn + 1) % 2
                w.img.setMouseTracking(True)
                w.img.loop = True
            else:
                while w.img.loop:
                    pygame.draw.rect(screen, COLOR[0], (0, 0, width, SQUARESIZE))
                    posx = w.img.xpos
                    col = posx // SQUARESIZE
                    draw_circle(-1, col, COLOR[turn + 1])
                    w.upd()
                    w.repaint()
                    QtTest.QTest.qWait(100)
                    if not w.img.loop:
                        break
                w.img.setMouseTracking(False)
                # human plays
                posx = w.img.xpos
                col = posx // SQUARESIZE
                if not put_piece(board, last_in_row, col, turn + 1):
                    w.img.setMouseTracking(True)
                    continue
                winsound.PlaySound('mixkit-small-hit-in-a-game-2072.wav', winsound.SND_ASYNC)
                draw_board(board)
                w.upd()
                w.repaint()
                scores[turn] = update_score(board, turn + 1)
                turn = (turn + 1) % 2
        app.exec_()

start()
>>>>>>> 39c399676760fc43fa754274862b0bd97d6bd254
