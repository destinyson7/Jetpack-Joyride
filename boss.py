from character import Character
from colorama import Fore, Back, Style
from data import *


class Boss(Character):
    def __init__(self):
        Character.__init__(self)

        self.lives = 5

        self.__coordinates = {}
        self.__display = []

        for i in range(13, 24):
            self.__coordinates[i] = []

            for j in range(columns - 38, columns - 5):
                self.__coordinates[i].append(j)

        with open('boss.txt', 'r') as f:
            pic = f.readlines()

            for i in pic:
                self.__display.append(list(i))
                # print(len(list(i)))

    def insert(self, board):

        x = 0
        for i in self.__coordinates:
            y = 0

            for j in self.__coordinates[i]:
                # print(x, y)
                board.grid[i][j].display = Back.BLACK + Fore.BLUE + Style.BRIGHT + \
                    self.__display[x][y] + Style.RESET_ALL
                y += 1

            x += 1
