class Car:
    """
    模拟汽车信息的类
    """
    def __init__(self, make, model, year):
        """
        初始化车辆描述信息
        """
        self.make = make
        self.model = model
        self.year = year
        # 初始化默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        返回标准格式的描述信息
        """
        return f'{self.year} {self.make} {self.model}'.title()
    
    def read_odometer(self):
        """
        读取里程表
        """
        return f'the car hsa {self.odometer_reading} miles on it...'
    
    def update_odometer(self, miles):
        """
        通过方法更改里程数
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('Invalid odometer reading! Please enter a positive number.')
    
