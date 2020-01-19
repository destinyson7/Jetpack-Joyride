from colorama import Fore, Back, Style
from data import *


class Coin:
    def __init__(self, x, y, board, number_of_coins):
        self.display = Fore.CYAN + '$' + Style.RESET_ALL
        self.present = True
        self.start = [x, y]
        self.number_of_coins = number_of_coins

        can = True

        for i in range(0, 2):
            for j in range(self.start[1], self.start[1] + self.number_of_coins + 1):
                if self.start[0] + i >= 0 and self.start[0] + i < rows and j >= 0 and j < columns:
                    if board.grid[self.start[0] + i][j].obstacle:
                        can = False
                        break
            if not can:
                break

        if can:
            for i in range(0, 2):
                for j in range(self.start[1], self.start[1] + self.number_of_coins + 1):
                    if self.start[0] + i >= 0 and self.start[0] + i < rows and j >= 0 and j < columns:
                        board.grid[self.start[0] + i][j].display = self.display
                        board.grid[self.start[0] + i][j].isCoin = True
