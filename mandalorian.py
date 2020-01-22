from character import Character
from colorama import Fore, Back, Style
from data import *
import math
from fire_beam import *
import time
from boost import Boost
from bullet import Bullet
import os
import sys


class Mandalorian(Character):
    def __init__(self):
        Character.__init__(self)
        self.__display = mando_display
        self.__shield_display = shield_display
        self.__coordinates = {
            25: [25],
            26: [25],
            27: [24, 26]
        }
        self.__shield = False
        self.__bullet_number = 0
        self.__centre = 26

        self.__game_over_display = []

        with open('loss.txt', 'r') as f:
            pic = f.readlines()

            for i in pic:
                # print(i)
                self.__game_over_display.append(list(i))

        # time.sleep(1)

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, shield):
        self.__shield = shield

    @property
    def bullet_number(self):
        return self.__bullet_number

    @bullet_number.setter
    def bullet_number(self, bullet_number):
        self.__bullet_number = bullet_number

    @property
    def centre(self):
        return self.__centre

    @centre.setter
    def centre(self, centre):
        self.__centre = centre

    def flash(self):
        # time.sleep(0.5)

        pr = ""
        pr += "\033[0;0H"
        pri = " " * (columnsAtATime + 10)
        pri += "\n"
        pr += pri * (16)
        pr += (Back.BLACK + " " + Style.RESET_ALL) * (int)(columnsAtATime / 2 - 3) + \
            Fore.GREEN + Style.BRIGHT + "Lives Remaining: " + \
            str(self.lives) + Style.RESET_ALL + "\n"
        pr += pri * (rows - 6)

        print(pr)

        time.sleep(0.5)

    def insert(self, board, boss, first_time):
        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                if board.grid[i][j].obstacle:
                    if not self.shield:
                        self.lives -= 1

                        if self.lives <= 0:
                            self.game_over()

                    FireBeam.erase(board.grid[i][j].beam_number, board)

                    if not self.shield:
                        self.flash()
                        board.show(self, boss, first_time)
                        time.sleep(0.5)
                        self.flash()

        centre_cnt = 0

        for i in self.__coordinates:
            centre_cnt += 1

            if centre_cnt == 2:
                self.centre = i

            for j in self.__coordinates[i]:

                if board.grid[i][j].isCoin:
                    self.score += 1
                    board.grid[i][j].isCoin = False

                elif board.grid[i][j].isBoost:
                    Boost.erase(board.grid[i][j].boost_number, board)

                    board.game_speed = min(1 + board.game_speed, 2)
                    board.speed_cnt = boost_length

                if self.shield:
                    board.grid[i][j].display = self.__shield_display

                else:
                    board.grid[i][j].display = self.__display

                board.grid[i][j].isPlayer = True

    def erase(self, board):
        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                board.grid[i][j].display = base_display
                board.grid[i][j].isPlayer = False

    def movey(self, y, board, boss, first_time):
        tmp = {}

        ma = -1
        mi = rows + 10

        for i in self.__coordinates:
            tmp[i + y] = self.__coordinates[i]
            mi = min(mi, i + y)
            ma = max(ma, i + y)

        if mi <= 0:
            tmp = {}
            rr = 0

            for i in self.__coordinates:
                tmp[rr] = self.__coordinates[i]
                rr += 1

        if ma >= rows - 1:
            tmp = {}
            rr = rows - 3

            for i in self.__coordinates:
                tmp[rr] = self.__coordinates[i]
                rr += 1

            self.onGround = True

        if ma < rows - 1:
            self.onGround = False

        else:
            self.onGround = True

        self.erase(board)
        self.__coordinates = tmp
        self.insert(board, boss, first_time)

    def movex(self, x, board, boss, first_time):
        tmp = {}

        last = -1
        first = columns + 10

        for i in self.__coordinates:
            tmp[i] = []

            for j in self.__coordinates[i]:
                tmp[i].append(j + x)
                last = max(last, j + x)
                first = min(first, j + x)

        if last >= (columns - 86):
            tmp = {}
            rr = 0

            for i in self.__coordinates:
                tmp[i] = []

                if rr < 2:
                    tmp[i].append(columns - 87)

                else:
                    tmp[i].append(columns - 88)
                    tmp[i].append(columns - 86)

                rr += 1

        elif last >= (board.curPos + columnsAtATime - 1):
            tmp = {}
            rr = 0

            for i in self.__coordinates:
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

            for i in self.__coordinates:
                tmp[i] = []

                if rr < 2:
                    tmp[i].append(board.curPos + 1)

                else:
                    tmp[i].append(board.curPos)
                    tmp[i].append(board.curPos + 2)

                rr += 1

        self.erase(board)
        self.__coordinates = tmp
        self.insert(board, boss, first_time)

    def free_fall(self, t, board, boss, first_time):

        y = (t * t) * 9.8
        y = y / 1000

        y = math.ceil(y)

        for i in range(y):
            self.movey(1, board, boss, first_time)

    def generate_bullet(self):

        count = 0

        for i in self.__coordinates:
            count += 1
            for j in self.__coordinates[i]:
                if count == 2:
                    x = i
                    y = j

                    break

            if count == 2:
                break

        Bullet(x, y, self.bullet_number)
        self.bullet_number += 1

    def game_over(self):

        os.system('clear')

        pr = ""

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 11

        for i in range(len(self.__game_over_display)):
            for j in range(len(self.__game_over_display[i])):

                pr += Fore.RED + Style.BRIGHT + \
                    self.__game_over_display[i][j] + Style.RESET_ALL

            # pr += "\n"

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 12

        pr += "\t" * 12 + Fore.YELLOW + Style.BRIGHT + \
            "Your Score: " + str(self.score) + Style.RESET_ALL

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 5

        print(pr)

        # time.sleep(2)
        sys.exit(0)

    def move_end(self, board, boss, first_time):

        prev = time.time()

        while True:
            cur = time.time()

            if cur - prev >= shift / 3:
                prev = cur
                tmp = {}

                last = -1
                first = columns + 10

                for i in self.__coordinates:
                    tmp[i] = []

                    for j in self.__coordinates[i]:
                        tmp[i].append(j + 1)
                        last = max(last, j + 1)
                        first = min(first, j + 1)

                self.erase(board)
                self.__coordinates = tmp
                self.insert(board, boss, first_time)

                board.show(self, boss, first_time)

                if last == columns - 1:
                    break
