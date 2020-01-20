from colorama import Fore, Back, Style
from data import *

beams = []


class FireBeam:
    def __init__(self, x, y, angle, board, beam_cnt):

        self.__angle = angle

        if self.__angle == [0, 1]:
            self.__display = Back.BLACK + Fore.YELLOW + '-' + Style.RESET_ALL

        elif self.__angle == [1, 0]:
            self.__display = Back.BLACK + Fore.YELLOW + '|' + Style.RESET_ALL

        elif self.__angle == [1, 1]:
            self.__display = Back.BLACK + Fore.YELLOW + '\\' + Style.RESET_ALL

        else:
            self.__display = Back.BLACK + Fore.YELLOW + '/' + Style.RESET_ALL

        self.__obstacle = True
        self.__present = True
        self.__start = [x, y]
        self.__beam_cnt = beam_cnt

        if self.__angle == [0, 1]:
            cur_beam_length = int(beam_length * 2.5)

        else:
            cur_beam_length = beam_length

        board.grid[self.__start[0]][self.__start[1]].display = beam_end
        board.grid[self.__start[0]][self.__start[1]].obstacle = True
        board.grid[self.__start[0]][self.__start[1]].beam_number = beam_cnt

        for i in range(cur_beam_length):
            curx = self.__start[0] + self.__angle[0] * (i + 1)
            cury = self.__start[1] + self.__angle[1] * (i + 1)

            if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                board.grid[curx][cury].display = self.__display
                board.grid[curx][cury].obstacle = True
                board.grid[curx][cury].beam_number = beam_cnt

        curx = self.__start[0] + self.__angle[0] * (cur_beam_length + 1)
        cury = self.__start[1] + self.__angle[1] * (cur_beam_length + 1)

        if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
            board.grid[curx][cury].display = beam_end
            board.grid[curx][cury].obstacle = True
            board.grid[curx][cury].beam_number = beam_cnt

        beams.append([x, y, angle, cur_beam_length + 2])

    def erase(beam_number, board):
        x = beams[beam_number][0]
        y = beams[beam_number][1]
        cur_angle = beams[beam_number][2]
        cur_beam_length = beams[beam_number][3]

        for k in range(cur_beam_length):
            curx = x + cur_angle[0] * k
            cury = y + cur_angle[1] * k

            if curx >= 0 and curx < rows and cury >= 0 and cury < columns:
                board.grid[curx][cury].display = base_display
                board.grid[curx][cury].obstacle = False
