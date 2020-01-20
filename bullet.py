from colorama import Fore, Back, Style
from data import *
from fire_beam import *

bullets = []


class Bullet:
    def __init__(self, x, y, bullet_number):
        self.__x = x
        self.__y = y
        self.__bullet_number = bullet_number
        self.__display = bullet_display
        self.__present = True

        bullets.append(self)

    def erase(bullet_number, board):

        for i in bullets:
            if i.__bullet_number == bullet_number:
                i.__present = False
                board.grid[i.__x][i.__y].display = base_display
                break

    def move(board, mandalorian):

        for i in bullets:

            if i.__present:
                x = i.__x
                y = i.__y

                if board.grid[x][y].isCoin:
                    display = coin_display

                elif board.grid[x][y].isBoost:
                    display = boost_display

                else:
                    display = base_display

                board.grid[x][y].display = display

                y += 1

                if y > (board.curPos + columnsAtATime):
                    Bullet.erase(i.__bullet_number, board)

                elif board.grid[x][y].obstacle:
                    FireBeam.erase(board.grid[x][y].beam_number, board)
                    Bullet.erase(i.__bullet_number, board)
                    mandalorian.score += 10

                else:
                    board.grid[x][y].display = bullet_display
                    i.__y += 1
