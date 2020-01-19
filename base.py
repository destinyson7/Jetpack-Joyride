from colorama import Fore, Back, Style
from data import *


class Base:
    def __init__(self):
        self.display = base_display
        self.obstacle = False
        self.beam_number = -1
        self.isCoin = False
        self.isBoost = False
