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

# size of circle and dimensions of board
SQUARESIZE = 100
ROWS = 6
COLUMNS = 7
K = 3 #max depth
P = 0 #pruning option
RADIUS = SQUARESIZE // 2 - 5
# Colors
COLOR = [(237, 237, 237), (255, 204, 92), (255, 111, 105)] #circle's colors
BOARD_COLOR = (88, 140, 126)

# screen size and dimensions
width = COLUMNS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)

# initialize BOARD
board = np.zeros((ROWS, COLUMNS), dtype=int)

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