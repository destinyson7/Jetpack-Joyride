import time
import signal
import os
from board import Board
from mandalorian import Mandalorian
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from input import *
from data import *
import sys

sys.stderr.write("\x1b[2J\x1b[H")
# Code for clear screen in UNIX machines

board = Board(rows, columns, columnsAtATime)
board.insert()
board.generate_beams()
board.generate_coins()
board.generate_boosts()

mandalorian = Mandalorian()
mandalorian.insert(board)

prev = time.time()
iteration = 0
t = 0

while True:

    iteration += 1
    board.speed_cnt -= 1

    if board.speed_cnt == 0:
        board.game_speed = 1
    # print("iter:", iteration)

    cur = time.time()
    if cur - prev >= shift:
        prev = cur
        board.curPos += 1 * board.game_speed
        for i in range(board.game_speed):
            mandalorian.movex(1, board)
        mandalorian.movey(0, board)
        board.show(mandalorian)

    char = user_input()

    if mandalorian.onGround:
        t = 0

    else:
        t += 1

    if char != 'w' and char != 'W':
        for i in range(board.game_speed):
            mandalorian.free_fall(t, board)

    if char == 'w' or char == 'W':
        for i in range(board.game_speed):
            mandalorian.movey(-1, board)
        t = 0

    elif char == 'a' or char == 'A':
        for i in range(board.game_speed):
            mandalorian.movex(-1, board)

    elif char == 'd' or char == 'D':
        for i in range(board.game_speed):
            mandalorian.movex(1, board)

    elif char == 'q' or char == 'Q':
        break

    if mandalorian.lives <= 0:
        break

    board.show(mandalorian)
