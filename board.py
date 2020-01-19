import numpy as np
from base import Base
from colorama import Fore, Back, Style
from data import *
import random
from fire_beam import FireBeam
from coin import Coin


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

        self.grid = np.array(self.grid)

    def show(self, mandalorian):

        pr = ""

        pr += "\033[0;0H"
        pr += "\n" * 4

        pr += "Lives Remaining: " + str(mandalorian.lives) + "\t" + "Score: " + str(mandalorian.score) + "\n"

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

        beam_cnt = 0

        for j in range(45, columns - beam_length - 3, 50):
            x = random.randint(0, rows - 3 - beam_length)
            y = j + random.randint(0, 25)

            a = random.randint(0, 3)
            angle = angles[a]

            FireBeam(x, y, angle, self, beam_cnt)

            beam_cnt += 1

    def generate_coins(self):

        for j in range(45, columns - 2, 29):
            x = random.randint(0, rows - 2)
            y = j + random.randint(0, 15)

            number_of_coins = random.randint(5, 10)

            # print(x, y, number_of_coins)

            Coin(x, y, self, number_of_coins)
