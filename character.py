from base import Base


class Character(Base):
    def __init__(self):
        Base.__init__(self)
        self.__score = 0
        self.__lives = 1
        self.__onGround = False

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        self.__lives = lives

    @property
    def onGround(self):
        return self.__onGround

    @onGround.setter
    def onGround(self, onGround):
        self.__onGround = onGround

    def movey(self, y, board):
        tmp = {}

        diff = 0

        for i in self.__coordinates:
            tmp[start + diff] = self.__coordinates[i]
            # print(start, diff, i, i + diff, "hehe")
            diff += 1

        self.__coordinates = tmp
