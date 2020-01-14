from character import Character
from colorama import Fore, Back, Style


class Mandalorian(Character):
    def __init__(self):
        Character.__init__(self)
        self.display = Back.RED + ' ' + Style.RESET_ALL

    def insert(self, board):
        for i in range(15, 18):
            for j in range(15, 18):
                board.grid[i][j].display = self.display
