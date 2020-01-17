import numpy as np
from base import Base
from colorama import Fore, Back, Style


class Board:

    def __init__(self, rows, columns, columnsAtATime):
        self.rows = rows
        self.columns = columns
        self.columnsAtATime = columnsAtATime
        self.curPos = 0
        self.base_display = Back.BLUE + ' ' + Style.RESET_ALL

    def insert(self):
        # self.grid = np.full((self.rows, self.columns), Base())

        self.grid = []

        for i in range(self.rows):

            tmp = []

            for j in range(self.columns):
                tmp.append(Base())

            self.grid.append(tmp)

    def show(self):
        pr = ""

        pr += "\033[0;0H"

        start = self.curPos
        end = start + self.columnsAtATime

        for i in range(self.rows):
            for j in range(start, end):
                pr += self.grid[i][j].display
            pr += "\n"

        for j in range(start, end):
            pr += self.base_display

        pr += "\n"

        print(pr)
