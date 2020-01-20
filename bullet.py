from colorama import Fore, Back, Style
from data import *
from fire_beam import *

bullets = []


class Bullet:
    def __init__(self, x, y, bullet_number):
        self.x = x
        self.y = y
        self.bullet_number = bullet_number
        self.display = bullet_display
        self.present = True

        bullets.append(self)

    def erase(bullet_number, board):

        for i in bullets:
            if i.bullet_number == bullet_number:
                i.present = False
                board.grid[i.x][i.y].display = base_display
                break

    def move(board, mandalorian):

        for i in bullets:

            if i.present:
                x = i.x
                y = i.y

                if board.grid[x][y].isCoin:
                    display = coin_display

                elif board.grid[x][y].isBoost:
                    display = boost_display

                else:
                    display = base_display

                board.grid[x][y].display = display

                y += 1

                if y > (board.curPos + columnsAtATime):
                    Bullet.erase(i.bullet_number, board)

                elif board.grid[x][y].obstacle:
                    FireBeam.erase(board.grid[x][y].beam_number, board)
                    Bullet.erase(i.bullet_number, board)

                else:
                    board.grid[x][y].display = bullet_display
                    i.y += 1
