from colorama import Fore, Back, Style
from data import *

beams = []


class FireBeam:
    def __init__(self, x, y, angle, board, beam_cnt):

        self.angle = angle

        if self.angle == [0, 1]:
            self.display = Fore.YELLOW + '-' + Style.RESET_ALL

        elif self.angle == [1, 0]:
            self.display = Fore.YELLOW + '|' + Style.RESET_ALL

        elif self.angle == [1, 1]:
            self.display = Fore.YELLOW + '\\' + Style.RESET_ALL

        else:
            self.display = Fore.YELLOW + '/' + Style.RESET_ALL

        self.obstacle = True
        self.present = True
        self.start = [x, y]
        self.beam_cnt = beam_cnt

        # print(self.angle)

        if self.angle == [0, 1]:
            cur_beam_length = int(beam_length * 2.5)

        else:
            cur_beam_length = beam_length

        board.grid[self.start[0]][self.start[1]].display = beam_end
        board.grid[self.start[0]][self.start[1]].obstacle = True
        board.grid[self.start[0]][self.start[1]].beam_number = beam_cnt

        for i in range(cur_beam_length):
            curx = self.start[0] + self.angle[0] * (i + 1)
            cury = self.start[1] + self.angle[1] * (i + 1)

            if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                board.grid[curx][cury].display = self.display
                board.grid[curx][cury].obstacle = True
                board.grid[curx][cury].beam_number = beam_cnt

        curx = self.start[0] + self.angle[0] * (cur_beam_length + 1)
        cury = self.start[1] + self.angle[1] * (cur_beam_length + 1)

        if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
            board.grid[curx][cury].display = beam_end
            board.grid[curx][cury].obstacle = True
            board.grid[curx][cury].beam_number = beam_cnt

        beams.append([x, y, angle, cur_beam_length + 2])
