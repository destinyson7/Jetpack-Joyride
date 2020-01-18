import numpy as np
from base import Base
from colorama import Fore, Back, Style
from data import *
import random
from fireBeam import FireBeam


class Board:

    def __init__(self, rows, columns, columnsAtATime):
        self.rows = rows
        self.columns = columns
        self.columnsAtATime = columnsAtATime
        self.curPos = 0

    def insert(self):
        # self.grid = np.full((self.rows, self.columns), Base())

        self.grid = []

        for i in range(self.rows):

            tmp = []

            for j in range(self.columns):
                tmp.append(Base())

            self.grid.append(tmp)

        # self.grid = np.array(self.grid)

    def show(self):

        pr = ""

        pr += "\033[0;0H"
        pr += "\n" * 4

        start = self.curPos
        end = start + self.columnsAtATime

        for i in range(2):
            pr += border_display * 3

            for j in range(start, end):
                pr += border_display

            pr += border_display * 3
            pr += "\n"

        for i in range(self.rows):
            pr += border_display * 3

            for j in range(start, end):
                pr += self.grid[i][j].display

            pr += border_display * 3
            pr += "\n"

        for i in range(2):
            pr += border_display * 3

            for j in range(start, end):
                pr += border_display

            pr += border_display * 3
            pr += "\n"

        print(pr)

    def generate_beams(self):

        for j in range(35, columns, 60):
            x = random.randint(0, rows - 1)
            y = j + random.randint(0, 25)

            a = random.randint(0, 3)
            angle = angles[a]

            FireBeam(x, y, angle, self)
