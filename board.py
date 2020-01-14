import numpy as np
from base import Base


class Board:

    def __init__(self, rows, columns, columnsAtATime):
        self.rows = rows
        self.columns = columns
        self.columnsAtATime = columnsAtATime
        self.curPos = 0

    def insert(self):
        self.grid = np.full((self.rows, self.columns), Base())

    def show(self, start):
        print("\033[0;0H")

        end = start + self.columnsAtATime

        for i in range(self.rows):
            for j in range(start, end):
                print(self.grid[i][j].display, end="")
            print()
