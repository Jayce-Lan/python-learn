from random import randint

class Die:
    """模拟一个骰子类"""
    def __init__(self, sides = 6):
        """初始化骰子的面数， 一般都为6面"""
        self.sides = sides
    
    def roll_die(self):
        """返回一个1到骰子面数之间的随机数"""
        return randint(1, self.sides)