from character import Character
from colorama import Fore, Back, Style
from data import *
import math
from fire_beam import *
import time
from boost import Boost
from bullet import Bullet


class Mandalorian(Character):
    def __init__(self):
        Character.__init__(self)
        self.display = mando_display
        self.shield_display = shield_display
        self.coordinates = {
            25: [25],
            26: [25],
            27: [24, 26]
        }
        self.shield = False
        self.bullet_number = 0

    def flash(self):
        # time.sleep(0.5)

        pr = ""
        pr += "\033[0;0H"
        pri = " " * (columnsAtATime + 10)
        pri += "\n"
        pr += pri * (16)
        pr += (Back.BLACK + " " + Style.RESET_ALL) * (int)(columnsAtATime / 2 - 3) + \
            Fore.GREEN + "Lives Remaining: " + str(self.lives) + Style.RESET_ALL + "\n"
        pr += pri * (rows - 6)

        print(pr)

        time.sleep(0.5)

    def insert(self, board):
        for i in self.coordinates:
            for j in self.coordinates[i]:
                if board.grid[i][j].obstacle:
                    if not self.shield:
                        self.lives -= 1

                    FireBeam.erase(board.grid[i][j].beam_number, board)

                    if not self.shield:
                        self.flash()
                        board.show(self)
                        time.sleep(0.5)
                        self.flash()

        for i in self.coordinates:
            for j in self.coordinates[i]:

                if board.grid[i][j].isCoin:
                    self.score += 1
                    board.grid[i][j].isCoin = False

                elif board.grid[i][j].isBoost:
                    Boost.erase(board.grid[i][j].boost_number, board)

                    board.game_speed = min(1 + board.game_speed, 2)
                    board.speed_cnt = boost_length

                if self.shield:
                    board.grid[i][j].display = self.shield_display

                else:
                    board.grid[i][j].display = self.display

    def erase(self, board):
        for i in self.coordinates:
            for j in self.coordinates[i]:
                board.grid[i][j].display = base_display

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
        y = y / 1000
        y = y / 5

        y = math.ceil(y)

        for i in range(y):
            self.movey(1, board)

    def generate_bullet(self):

        count = 0

        for i in self.coordinates:
            count += 1
            for j in self.coordinates[i]:
                if count == 2:
                    x = i
                    y = j

                    break

            if count == 2:
                break

        Bullet(x, y, self.bullet_number)
        self.bullet_number += 1
