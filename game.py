import time
import signal
import os
from board import Board
from mandalorian import Mandalorian
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from input import *

board = Board(50, 20000, 200)
board.insert()
mandalorian = Mandalorian()
mandalorian.insert(board)

while True:

    char = user_input()

    if char == 'w':
        pass
    elif char == 's':
        pass
    elif char == 'a':
        pass
    elif char == 'd':
        pass
