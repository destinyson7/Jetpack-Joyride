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

    def movey(self, x, board):
        tmp = {}

        for i in self.coordinates:
            tmp[i + x] = self.coordinates[i]

        self.erase(board)
        self.coordinates = tmp
        self.insert(board)

    def movex(self, y, board):
        tmp = {}

        for i in self.coordinates:
            tmp[i] = []

            for j in self.coordinates[i]:
                tmp[i].append(j + y)

        self.erase(board)
        self.coordinates = tmp
        self.insert(board)

    def free_fall(self, t, board):

        y = (t * t) * 9.8
        y = y / 100
        y = y / 5

        y = math.ceil(y)

        self.movey(y, board)
