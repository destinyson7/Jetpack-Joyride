import numpy as np
from base import Base
from colorama import Fore, Back, Style
from data import *
import random
from fire_beam import FireBeam
from coin import Coin
from boost import Boost


class Board:

    def __init__(self, rows, columns, columnsAtATime):
        self.__rows = rows
        self.__columns = columns
        self.__columnsAtATime = columnsAtATime
        self.curPos = 0
        self.game_speed = 1
        self.speed_cnt = 0
        self.shield_cnt = 0
        self.shield_cooloff = shield_cooloff

    def insert(self):
        # self.grid = np.full((self.rows, self.columns), Base())

        self.grid = []

        for i in range(self.__rows):

            tmp = []

            for j in range(self.__columns):
                tmp.append(Base())

            self.grid.append(tmp)

        self.grid = np.array(self.grid)

    def show(self, mandalorian, boss):

        pr = ""

        pr += "\033[0;0H"
        pr += "\n" * 4

        pr += "Lives: " + Fore.RED + "❤ " * mandalorian.lives + \
            Style.RESET_ALL + "\t" + "Score: " + str(mandalorian.score)

        if self.curPos >= columns - columnsAtATime - 41:
            pr += "\t\t\t" + "Boss Lives: " + str(boss.lives) + "  " + "\n"

        else:
            pr += "\n"

        start = min(self.curPos, columns - columnsAtATime)
        end = start + self.__columnsAtATime

        for i in range(2):
            pr += border_display * 3

            for j in range(start, end):
                pr += border_display

            pr += border_display * 3
            pr += "\n"

        for i in range(self.__rows):
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

        for j in range(85, columns - columnsAtATime - 35, 49):
            x = random.randint(0, rows - 3 - beam_length)
            y = j + random.randint(0, 25)

            a = random.randint(0, 3)
            angle = angles[a]

            FireBeam(x, y, angle, self, beam_cnt)

            beam_cnt += 1

    def generate_coins(self):

        for j in range(78, columns - columnsAtATime - 25, 29):
            x = random.randint(0, rows - 2)
            y = j + random.randint(0, 15)

            number_of_coins = random.randint(5, 10)

            # print(x, y, number_of_coins)

            Coin(x, y, self, number_of_coins)

    def generate_boosts(self):

        boost_cnt = 0

        for j in range(73, columns - columnsAtATime - 25, 109):
            x = random.randint(0, rows - 8)
            y = j + random.randint(0, 15)

            Boost(x, y, self, boost_cnt)

            boost_cnt += 1
