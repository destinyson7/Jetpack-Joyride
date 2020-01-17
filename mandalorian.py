from character import Character
from colorama import Fore, Back, Style
from data import *
import math


class Mandalorian(Character):
    def __init__(self):
        Character.__init__(self)
        self.display = Back.RED + ' ' + Style.RESET_ALL
        self.coordinates = {
            25: [25],
            26: [25],
            27: [24, 26]
        }
        self.base_display = Back.BLUE + ' ' + Style.RESET_ALL

    def insert(self, board):
        for i in self.coordinates:
            for j in self.coordinates[i]:
                board.grid[i][j].display = self.display

    def erase(self, board):
        for i in self.coordinates:
            for j in self.coordinates[i]:
                board.grid[i][j].display = self.base_display

    def movey(self, y, board):
        tmp = {}

        ma = -1
        mi = rows + 10

        for i in self.coordinates:
            tmp[i + y] = self.coordinates[i]
            mi = min(mi, i + y)
            ma = max(ma, i + y)

        if mi <= 0:
            tmp = {}
            rr = 0

            for i in self.coordinates:
                tmp[rr] = self.coordinates[i]
                rr += 1

        if ma >= rows - 1:
            tmp = {}
            rr = rows - 3

            for i in self.coordinates:
                tmp[rr] = self.coordinates[i]
                rr += 1

            self.onGround = True

        if ma < rows - 1:
            self.onGround = False

        else:
            self.onGround = True

        self.erase(board)
        self.coordinates = tmp
        self.insert(board)

    def movex(self, x, board):
        tmp = {}

        last = -1
        first = columns + 10

        for i in self.coordinates:
            tmp[i] = []

            for j in self.coordinates[i]:
                tmp[i].append(j + x)
                last = max(last, j + x)
                first = min(first, j + x)

        # print(first, last, "###" + str(board.curPos) + "###")

        if last >= (board.curPos + columnsAtATime - 1):
            tmp = {}
            rr = 0

            for i in self.coordinates:
                tmp[i] = []

                if rr < 2:
                    tmp[i].append(board.curPos + columnsAtATime - 2)

                else:
                    tmp[i].append(board.curPos + columnsAtATime - 3)
                    tmp[i].append(board.curPos + columnsAtATime - 1)

                rr += 1

        if first <= board.curPos:
            tmp = {}
            rr = 0

            for i in self.coordinates:
                tmp[i] = []

                if rr < 2:
                    tmp[i].append(board.curPos + 1)

                else:
                    tmp[i].append(board.curPos)
                    tmp[i].append(board.curPos + 2)

                rr += 1

        self.erase(board)
        self.coordinates = tmp
        self.insert(board)

    def free_fall(self, t, board):

        y = (t * t) * 9.8
        y = y / 100
        y = y / 5

        y = math.ceil(y)

        self.movey(y, board)
