from colorama import Fore, Back, Style
from data import *


class Base:
    def __init__(self):
        self.__display = base_display
        self.__obstacle = False
        self.__beam_number = -1
        self.__isCoin = False
        self.__isBoost = False
        self.__boost_number = -1
        self.__isPlayer = False
        self.__isEnemy = False
        self.__isBullet = False
        self.__bullet_num = -1
        self.__isIceBall = False

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display

    @property
    def obstacle(self):
        return self.__obstacle

    @obstacle.setter
    def obstacle(self, obstacle):
        self.__obstacle = obstacle

    @property
    def beam_number(self):
        return self.__beam_number

    @beam_number.setter
    def beam_number(self, beam_number):
        self.__beam_number = beam_number

    @property
    def isCoin(self):
        return self.__isCoin

    @isCoin.setter
    def isCoin(self, isCoin):
        self.__isCoin = isCoin

    @property
    def isBoost(self):
        return self.__isBoost

    @isBoost.setter
    def isBoost(self, isBoost):
        self.__isBoost = isBoost

    @property
    def boost_number(self):
        return self.__boost_number

    @boost_number.setter
    def boost_number(self, boost_number):
        self.__boost_number = boost_number

    @property
    def isPlayer(self):
        return self.__isPlayer

    @isPlayer.setter
    def isPlayer(self, isPlayer):
        self.__isPlayer = isPlayer

    @property
    def isEnemy(self):
        return self.__isEnemy

    @isEnemy.setter
    def isEnemy(self, isEnemy):
        self.__isEnemy = isEnemy

    @property
    def isBullet(self):
        return self.__isBullet

    @isBullet.setter
    def isBullet(self, isBullet):
        self.__isBullet = isBullet

    @property
    def bullet_num(self):
        return self.__bullet_num

    @bullet_num.setter
    def bullet_num(self, bullet_num):
        self.__bullet_num = bullet_num

    @property
    def isIceBall(self):
        return self.__isIceBall

    @isIceBall.setter
    def isIceBall(self, isIceBall):
        self.__isIceBall = isIceBall
