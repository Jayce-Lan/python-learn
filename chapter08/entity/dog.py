class Dog:
    """
    模拟小狗的简单尝试
    """
    def __init__(self, name, age):
        """
        初始化小狗的姓名和年龄
        """
        self.name = name
        self.age = age
    
    def sit(self):
        """
        让小狗坐下
        """
        return f'{self.name} is sitting...'
    
    def roll_over(self):
        """
        让小狗打滚
        """
        return f'{self.name} rolled over!'