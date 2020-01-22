from character import Character
from colorama import Fore, Back, Style
from data import *
from ice_ball import IceBall
import os
import sys


class Boss(Character):
    def __init__(self):
        Character.__init__(self)

        self.lives = 10

        self.__coordinates = {}
        self.__display = []
        self.__centre = 18
        self.__ice_ball_number = 0

        for i in range(13, 24):
            self.__coordinates[i] = []

            for j in range(columns - 38, columns - 5):
                self.__coordinates[i].append(j)

        with open('boss.txt', 'r') as f:
            pic = f.readlines()

            for i in pic:
                self.__display.append(list(i))
                # print(len(list(i)))

        self.__game_over_display = []

        with open('win.txt', 'r') as f:
            pic = f.readlines()

            for i in pic:
                # print(i)
                self.__game_over_display.append(list(i))

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
        centre_cnt = 0
        for i in self.__coordinates:
            centre_cnt += 1

            if centre_cnt == 6:
                self.__centre = i

            y = 0

            for j in self.__coordinates[i]:
                # print(i, j)
                board.grid[i][j].display = Back.BLACK + Fore.RED + Style.BRIGHT + \
                    self.__display[x][y] + Style.RESET_ALL

                if self.__display[x][y] != ' ':
                    board.grid[i][j].isEnemy = True

                y += 1

            x += 1

    def movey(self, y, board):
        start = max(0, self.__centre + y - 5)
        start = min(start, rows - 11)

        # print(start)

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

    def generate_ice_balls(self):

        IceBall(self.__centre - 4, columns - 34, self.__ice_ball_number)
        self.__ice_ball_number += 1

        IceBall(self.__centre, columns - 24, self.__ice_ball_number)
        self.__ice_ball_number += 1

        IceBall(self.__centre + 4, columns - 23, self.__ice_ball_number)
        self.__ice_ball_number += 1

    def game_over(self, mandalorian):

        os.system('clear')

        pr = ""

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 11

        for i in range(len(self.__game_over_display)):
            for j in range(len(self.__game_over_display[i])):

                pr += Fore.GREEN + Style.BRIGHT + \
                    self.__game_over_display[i][j] + Style.RESET_ALL

            # pr += "\n"

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 12

        pr += "\t" * 12 + Fore.YELLOW + Style.BRIGHT + \
            "Your Score: " + str(mandalorian.score) + Style.RESET_ALL

        pr += (Back.BLACK + Style.BRIGHT + "\n" + Style.RESET_ALL) * 5

        print(pr)

        # time.sleep(2)
        sys.exit(0)
