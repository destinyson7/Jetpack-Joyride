import time
from board import Board
from mandalorian import Mandalorian

board = Board(50, 20000, 200)
board.insert()
mandalorian = Mandalorian()
mandalorian.insert(board)

while True:
    board.show(board.curPos)
    time.sleep(0.15)
    board.curPos += 1
