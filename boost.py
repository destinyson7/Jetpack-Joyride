from colorama import Fore, Back, Style
from data import *

boosts = []


class Boost:
    def __init__(self, x, y, board, boost_cnt):
        self.display = boost_display
        self.present = True
        self.start = [x, y]

        self.position = {

            x: [y, y + 1, y + 3, y + 4],
            x + 1: [y + 1, y + 2, y + 4, y + 5],
            x + 2: [y + 2, y + 3, y + 5, y + 6],
            x + 3: [y + 1, y + 2, y + 4, y + 5],
            x + 4: [y, y + 1, y + 3, y + 4]
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
                        board.grid[i][j].boost_number = boost_cnt

        boosts.append(self.position)

    def erase(boost_number, board):
        for i in boosts[boost_number]:
            for j in boosts[boost_number][i]:

                curx = i
                cury = j

                if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                    board.grid[curx][cury].display = base_display
