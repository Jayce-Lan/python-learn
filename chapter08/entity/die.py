from random import randint

class Die:
    """
    模拟一个骰子类
    """
    def __init__(self, sides=6):
        """
        初始化骰子的面数
        """
        self.sides = sides

    def roll_die(self):
        """
        投掷骰子
        """
        return randint(1, self.sides)
    