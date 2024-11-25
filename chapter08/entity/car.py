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
        self.gas_tank_capacity = 100  # 假设100L

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

    def fill_gas_tank(self):
        """
        油箱容量
        """
        return f'this car has {self.gas_tank_capacity} miles'

    
# ----------------------------------------------------------------
# 继承父类
# 创建一个电动车类，用于继承父类，并且存在一些自己的特殊方法
# ----------------------------------------------------------------
class ElectricCar(Car):
    """
    继承自Car的ElectricCar类
    """
    def __init__(self, make, model, year):
        """
        初始化父类属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """
        重写父类方法
        """
        return 'electric car is doesn\'t has a gas tank!'
    
    def get_range(self):
        """
        获取电动车剩余里程
        """
        if self.battery.get_battery_range() < 10:
            return 'This car has a range of 10 miles on a full charge.'
        elif self.battery.get_battery_range() < 50:
            return 'This car has a range of 20 miles on a full charge.'
        elif self.battery.get_battery_range() < 100:
            return 'This car has a range of 50 miles on a full charge.'
        else:
            return 'This car has a range of 100 miles on a full charge.'


# ----------------------------------------------------------------
# 存储电池信息
# ----------------------------------------------------------------
class Battery:
    """
    存储电池信息
    """
    def __init__(self, battery_size=70):
        """
        初始化电池容量
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        打印电池容量
        """
        return f'This car has a {self.battery_size}-kWh battery.'
    
    def get_battery_range(self):
        return self.battery_size
