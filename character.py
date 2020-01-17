from base import Base


class Character(Base):
    def __init__(self):
        Base.__init__(self)
        self.score = 0
        self.lives = 3
        self.onGround = False
