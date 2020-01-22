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
from bullet import Bullet
from boss import Boss
from ice_ball import IceBall

sys.stderr.write("\x1b[2J\x1b[H")
# Code for clear screen in UNIX machines

board = Board(rows, columns, columnsAtATime)
board.insert()
board.generate_beams()
board.generate_coins()
board.generate_boosts()

mandalorian = Mandalorian()
mandalorian.insert(board)

boss = Boss()
boss.insert(board)

prev = time.time()
prev_ball = prev
iteration = 0
t = 0

while True:

    iteration += 1
    board.speed_cnt = max(board.speed_cnt - 1, 0)
    board.shield_cnt = max(board.shield_cnt - 1, 0)

    if board.speed_cnt == 0:
        board.game_speed = 1

    if board.shield_cnt == 0:
        mandalorian.shield = False
        board.shield_cooloff += 1

    # print("iter:", iteration)

    cur = time.time()
    if cur - prev >= shift:
        prev = cur

        board.curPos += 1 * board.game_speed

        if (cur - prev_ball) >= 2:
            if board.curPos >= (columns - columnsAtATime - 41):
                boss.generate_ice_balls()
                prev_ball = cur

        if board.curPos < (columns - columnsAtATime):
            for i in range(board.game_speed):
                mandalorian.movex(1, board)

        else:
            board.curPos = columns - columnsAtATime

        for i in range(4 * board.game_speed):
            Bullet.move(board, mandalorian, boss)

            if board.curPos >= (columns - columnsAtATime - 41):
                IceBall.move(board, mandalorian, boss)

        mandalorian.movey(0, board)

        board.show(mandalorian, boss)

    char = user_input()

    if mandalorian.onGround:
        t = 0

    else:
        t += 1

    if char != 'w' and char != 'W':
        for i in range(board.game_speed):
            mandalorian.free_fall(t, board)
            boss.move(board, mandalorian)

    if char == 'w' or char == 'W':
        for i in range(board.game_speed):
            mandalorian.movey(-1, board)
            boss.move(board, mandalorian)
        t = 0

    elif char == 'a' or char == 'A':
        for i in range(board.game_speed):
            mandalorian.movex(-1, board)

    elif char == 'd' or char == 'D':
        for i in range(board.game_speed):
            mandalorian.movex(1, board)

    elif char == 'q' or char == 'Q':
        break

    elif char == ' ':
        if board.shield_cooloff >= shield_cooloff:
            mandalorian.shield = True
            board.shield_cnt = shield_length
            board.shield_cooloff = 0

    elif char == 'r' or char == 'R':
        mandalorian.generate_bullet()

    if mandalorian.lives <= 0:
        # TODO: display game over screen
        break

    board.show(mandalorian, boss)
