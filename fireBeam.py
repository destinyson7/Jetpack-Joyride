from base import Base
from colorama import Fore, Back, Style
from data import *

beams = []


class FireBeam:
    def __init__(self, x, y, angle, board, beam_cnt):
        self.display = Fore.YELLOW + 'B' + Style.RESET_ALL
        self.obstacle = True
        self.present = True
        self.start = [x, y]
        self.angle = angle
        self.beam_cnt = beam_cnt

        # print(self.angle)

        if self.angle == [0, 1]:
            cur_beam_length = beam_length * 3

        else:
            cur_beam_length = beam_length

        for i in range(cur_beam_length):
            curx = self.start[0] + self.angle[0] * i
            cury = self.start[1] + self.angle[1] * i

            if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                board.grid[curx][cury].display = self.display
                board.grid[curx][cury].obstacle = True

        beams.append([x, y, angle])
