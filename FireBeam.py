from base import Base
from colorama import Fore, Back, Style
from data import *


class FireBeam(Base):
    def __init__(self, x, y, angle, board):
        self.display = Fore.YELLOW + "B" + Style.RESET_ALL
        self.obstacle = True
        self.present = True
        self.start = [x, y]
        self.angle = angle

        for i in range(beam_length):
            curx = start[0] + angle[0] * i
            cury = start[1] + angle[1] * i
