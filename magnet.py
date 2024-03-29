from colorama import Fore, Back, Style
from data import *

magnets = []


class Magnet:
    def __init__(self, x, y, board, magnet_cnt):
        self.__present = True
        self.__start = [x, y]

        self.__coordinates = {

            x - 1: [y],
            x: [y - 1, y, y + 1],
            x + 1: [y]
        }

        self.__display = [
            ['M'],
            ['M', 'M', 'M'],
            ['M']
        ]

        can = True

        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                if i >= 0 and i < rows and j >= 0 and j < columns:
                    if board.grid[i][j].obstacle or board.grid[i][j].isCoin or board.grid[i][j].isBoost:
                        can = False
                        break
            if not can:
                break

        if can:
            xx = 0
            for i in self.__coordinates:
                yy = 0

                for j in self.__coordinates[i]:
                    board.grid[i][j].display = Back.BLACK + Fore.RED + Style.BRIGHT + \
                        self.__display[xx][yy] + Style.RESET_ALL

                    yy += 1

                xx += 1

        else:
            self.__present = False

        magnets.append(self)

    def show(self, board):
        xx = 0
        for i in self.__coordinates:
            yy = 0

            for j in self.__coordinates[i]:
                board.grid[i][j].display = Back.BLACK + Fore.RED + Style.BRIGHT + \
                    self.__display[xx][yy] + Style.RESET_ALL

                yy += 1

            xx += 1

    def attract(board, mandalorian, boss, first_time):

        flag = False

        for i in magnets:

            if i.__present:

                if i.__start[1] >= board.curPos and i.__start[1] < (board.curPos + columnsAtATime):

                    flag = True

                    mando_pos = list(mandalorian.coordinates.keys())
                    mando_pos.sort()
                    x = mando_pos[1]
                    y = mandalorian.coordinates[x][0]

                    # print(x, y, i.__start[0], i.__start[1])

                    if x < i.__start[0]:
                        for j in range(2):
                            mandalorian.movey(1, board, boss, first_time)

                    elif x > i.__start[0]:
                        for j in range(2):
                            mandalorian.movey(-1, board, boss, first_time)

                    if y < i.__start[1]:
                        for j in range(2):
                            mandalorian.movex(1, board, boss, first_time)

                    elif y > i.__start[1]:
                        for j in range(2):
                            mandalorian.movex(-1, board, boss, first_time)

                i.show(board)

        return flag
