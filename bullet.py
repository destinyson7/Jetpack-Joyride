from colorama import Fore, Back, Style
from data import *


class Bullet:
    def __init__(self, x, y, bullet_number):
        self.x = x
        self.y = y
        self.bullet_number = bullet_number
        self.display = bullet_display
