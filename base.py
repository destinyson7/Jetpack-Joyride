from colorama import Fore, Back, Style
from data import *


class Base:
    def __init__(self):
        self.display = base_display
        self.obstacle = False
        self.beam_number = -1
        self.isCoin = False
        self.isBoost = False
        self.boost_number = -1
        self.isPlayer = False
        self.isEnemy = False
        self.isBullet = False
        self.bullet_num = -1
        self.isIceBall = False
