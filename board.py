import numpy as np
from base import Base
from colorama import Fore, Back, Style
from data import *
import random
from fire_beam import FireBeam
from coin import Coin
from boost import Boost
from magnet import Magnet
import time
import sys


class Board:

    def __init__(self, rows, columns, columnsAtATime):
        self.__rows = rows
        self.__columns = columns
        self.__columnsAtATime = columnsAtATime
        self.__curPos = 0
        self.__game_speed = 1
        self.__speed_cnt = 0
        self.__shield_cnt = 0
        self.__shield_cooloff = shield_cooloff

    @property
    def curPos(self):
        return self.__curPos

    @curPos.setter
    def curPos(self, curPos):
        self.__curPos = curPos

    @property
    def game_speed(self):
        return self.__game_speed

    @game_speed.setter
    def game_speed(self, game_speed):
        self.__game_speed = game_speed

    @property
    def speed_cnt(self):
        return self.__speed_cnt

    @speed_cnt.setter
    def speed_cnt(self, speed_cnt):
        self.__speed_cnt = speed_cnt

    @property
    def shield_cnt(self):
        return self.__shield_cnt

    @shield_cnt.setter
    def shield_cnt(self, shield_cnt):
        self.__shield_cnt = shield_cnt

    @property
    def shield_cooloff(self):
        return self.__shield_cooloff

    @shield_cooloff.setter
    def shield_cooloff(self, shield_cooloff):
        self.__shield_cooloff = shield_cooloff

    def insert(self):
        # self.grid = np.full((self.rows, self.columns), Base())

        self.grid = []

        for i in range(self.__rows):

            tmp = []

            for j in range(self.__columns):
                tmp.append(Base())

            self.grid.append(tmp)

        self.grid = np.array(self.grid)

    def show(self, mandalorian, boss, first_time):

        pr = ""

        pr += "\033[0;0H"

        pr += Back.BLACK + Style.BRIGHT

        pr += "\n" * 4

        pr += "Lives: " + Back.BLACK + Fore.RED + "❤ " * mandalorian.lives + \
            Style.RESET_ALL + "\t" + "Score: " + str(mandalorian.score)

        time_remaining = int(max_time - (time.time() - first_time))

        if time_remaining <= 0:
            mandalorian.game_over()

        pr += "\t\t\t" + "Time Remaining: " + str(time_remaining).zfill(3)

        if self.curPos >= columns - columnsAtATime - 41:
            pr += "\t\t\t" + "Boss Lives: " + str(boss.lives) + "  "

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

        pr += Style.RESET_ALL

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

    def generate_magnets(self):

        magnet_cnt = 0

        for j in range(200, columns - columnsAtATime - 25, 401):
            x = random.randint(5, rows - 5)
            y = j + random.randint(0, 15)

            Magnet(x, y, self, magnet_cnt)

            magnet_cnt += 1
