from colorama import Fore, Back, Style
from data import *
from fire_beam import *
import sys
from bullet import Bullet

ice_balls = []


class IceBall:
    def __init__(self, x, y, ice_ball_number):
        self.__ice_ball_number = ice_ball_number
        self.__present = True

        self.__start = [x, y]

        self.display = ['<', '-', '-']

        ice_balls.append(self)

    def erase(ice_ball_number, board):

        for i in ice_balls:
            if i.__ice_ball_number == ice_ball_number:
                i.__present = False

                for j in range(3):
                    board.grid[i.__start[0]][i.__start[1] + j].display = base_display
                    board.grid[i.__start[0]][i.__start[1] + j].isIceBall = False

    def insert(self, board):

        for i in range(3):

            if (self.__start[1] + i) > columns - columnsAtATime:
                board.grid[self.__start[0]][self.__start[1] + i].display = Back.BLACK + \
                    Fore.BLUE + Style.BRIGHT + self.display[i] + Style.RESET_ALL
                board.grid[self.__start[0]][self.__start[1] + i].isIceBall = True

    def move(board, mandalorian, boss):

        for i in ice_balls:

            if i.__present:
                x = i.__start[0]
                y = i.__start[1]

                for j in range(0, 3):
                    board.grid[x][y + j].display = base_display
                    board.grid[x][y + j].isIceBall = False

                y -= 1
                i.__start[1] -= 1

                if y + 2 <= (columns - columnsAtATime):
                    IceBall.erase(i.__ice_ball_number, board)

                elif board.grid[x][y].isPlayer:

                    if not mandalorian.shield:
                        mandalorian.lives -= 1

                        mandalorian.flash()

                        if mandalorian.lives <= 0:
                            sys.exit(0)

                    else:
                        mandalorian.shield = False
                        board.shield_cnt = 0

                    IceBall.erase(i.__ice_ball_number, board)

                elif board.grid[x][y].isBullet:
                    IceBall.erase(i.__ice_ball_number, board)
                    Bullet.erase(board.grid[x][y].bullet_num, board)

                elif board.grid[x][y - 1].isBullet:
                    IceBall.erase(i.__ice_ball_number, board)
                    Bullet.erase(board.grid[x][y - 1].bullet_num, board)

                elif board.grid[x][y].obstacle:
                    FireBeam.erase(board.grid[x][y].beam_number, board)
                    IceBall.erase(i.__ice_ball_number, board)

                else:
                    IceBall.insert(i, board)
