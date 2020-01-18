from base import Base
from colorama import Fore, Back, Style
from data import *


class FireBeam:
    def __init__(self, x, y, angle, board):
        self.display = Back.CYAN + Fore.YELLOW + "B " + Style.RESET_ALL
        self.obstacle = True
        self.present = True
        self.start = [x, y]
        self.angle = angle

        for i in range(beam_length):
            curx = self.start[0] + self.angle[0] * i
            cury = self.start[1] + self.angle[1] * i

            if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                board.grid[curx][cury].display = self.display
                board.grid[curx][cury].obstacle = True
