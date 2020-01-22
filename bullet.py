from colorama import Fore, Back, Style
from data import *
from fire_beam import *
import sys

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
                board.grid[i.__x][i.__y].isBullet = False
                break

    def move(board, mandalorian, boss, first_time):

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
                board.grid[x][y].isBullet = False

                y += 1

                if y == columns - 1:
                    Bullet.erase(i.__bullet_number, board)

                elif y > (board.curPos + columnsAtATime):
                    Bullet.erase(i.__bullet_number, board)

                elif board.grid[x][y].isEnemy:
                    boss.lives -= 1
                    mandalorian.score += 15

                    if boss.lives <= 0:
                        boss.erase(board)
                        mandalorian.move_end(board, boss, first_time)
                        boss.game_over(mandalorian)
                        # sys.exit(0)

                    Bullet.erase(i.__bullet_number, board)

                elif board.grid[x][y].isIceBall:
                    Bullet.erase(i.__bullet_number, board)

                elif board.grid[x][y].obstacle:
                    FireBeam.erase(board.grid[x][y].beam_number, board)
                    Bullet.erase(i.__bullet_number, board)
                    mandalorian.score += 10

                else:
                    board.grid[x][y].display = bullet_display
                    board.grid[x][y].isBullet = True
                    board.grid[x][y].bullet_num = i.__bullet_number
                    i.__y += 1
