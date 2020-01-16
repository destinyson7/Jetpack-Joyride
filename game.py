import time
import signal
import os
from board import Board
from mandalorian import Mandalorian
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from input import *
from data import *

board = Board(rows, columns, columnsAtATime)
board.insert()

mandalorian = Mandalorian()
mandalorian.insert(board)

prev = time.time()
iteration = 0
t = 0

while True:

    iteration += 1
    print("iter:", iteration)

    cur = time.time()
    if cur - prev >= shift:
        prev = cur
        board.curPos += 1
        board.show()

    char = user_input()

    if char != 'w' and char != 'W':
        mandalorian.free_fall(t, board)
        t += 1

    if char == 'w' or char == 'W':
        mandalorian.movey(-1, board)

    elif char == 'a' or char == 'A':
        mandalorian.movex(-1, board)
        t = 0

    elif char == 'd' or char == 'D':
        mandalorian.movex(1, board)
        t = 0

    board.show()
