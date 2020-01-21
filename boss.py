from character import Character
from colorama import Fore, Back, Style
from data import *


class Boss(Character):
    def __init__(self):
        Character.__init__(self)

        self.lives = 5

        self.__coordinates = {}
        self.__display = []
        self.__centre = 18

        for i in range(13, 24):
            self.__coordinates[i] = []

            for j in range(columns - 38, columns - 5):
                self.__coordinates[i].append(j)

        with open('boss.txt', 'r') as f:
            pic = f.readlines()

            for i in pic:
                self.__display.append(list(i))
                # print(len(list(i)))

    def erase(self, board):
        x = 0
        for i in self.__coordinates:
            y = 0

            for j in self.__coordinates[i]:
                board.grid[i][j].display = base_display
                board.grid[i][j].isEnemy = False

                y += 1

            x += 1

    def insert(self, board):

        x = 0
        for i in self.__coordinates:
            y = 0

            for j in self.__coordinates[i]:
                # print(i, j)
                board.grid[i][j].display = Back.BLACK + Fore.BLUE + Style.BRIGHT + \
                    self.__display[x][y] + Style.RESET_ALL

                board.grid[i][j].isEnemy = True

                y += 1

            x += 1

    def movey(self, y, board):
        start = max(0, self.__centre + y - 5)
        start = min(start, rows - 11)

        print(start)

        tmp = {}

        diff = 0

        for i in self.__coordinates:
            tmp[start + diff] = self.__coordinates[i]
            # print(start, diff, i, i + diff, "hehe")
            diff += 1

        self.erase(board)
        self.__coordinates = tmp
        self.insert(board)

    def move(self, board, mandalorian):
        y = mandalorian.centre - self.__centre
        # print(mandalorian.centre, self.__centre)
        self.movey(y, board)
