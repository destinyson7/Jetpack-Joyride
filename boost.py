from colorama import Fore, Back, Style
from data import *


class Boost:
    def __init__(self, x, y, board):
        self.display = '>'
        self.present = True
        self.start = [x, y]

        self.position = {

            # x - 3: [y + 1],
            x - 2: [y + 2],
            x - 1: [y, y + 1, y + 2, y + 3],
            # x: [y, y + 1, y + 2, y + 3, y + 4],
            x: [y, y + 1, y + 2, y + 3],
            x + 1: [y + 2],
            # x + 3: [y + 1]
        }

        can = True

        for i in self.position:
            for j in self.position[i]:
                if i >= 0 and i < rows and j >= 0 and j < columns:
                    if board.grid[i][j].obstacle or board.grid[i][j].isCoin:
                        can = False
                        break
            if not can:
                break

        if can:
            for i in self.position:
                for j in self.position[i]:
                    if i >= 0 and i < rows and j >= 0 and j < columns:
                        board.grid[i][j].display = self.display
                        board.grid[i][j].isBoost = True
