from colorama import Fore, Back, Style
from data import *


class Coin:
    def __init__(self, x, y, board, number_of_coins):
        self.__display = coin_display
        self.__present = True
        self.__start = [x, y]
        self.__number_of_coins = number_of_coins

        can = True

        for i in range(0, 2):
            for j in range(self.__start[1], self.__start[1] + self.__number_of_coins + 1):
                if self.__start[0] + i >= 0 and self.__start[0] + i < rows and j >= 0 and j < columns:
                    if board.grid[self.__start[0] + i][j].obstacle:
                        can = False
                        break
            if not can:
                break

        if can:
            for i in range(0, 2):
                for j in range(self.__start[1], self.__start[1] + self.__number_of_coins + 1):
                    if self.__start[0] + i >= 0 and self.__start[0] + i < rows and j >= 0 and j < columns:
                        board.grid[self.__start[0] + i][j].display = self.__display
                        board.grid[self.__start[0] + i][j].isCoin = True
