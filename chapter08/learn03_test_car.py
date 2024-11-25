# 导入一个文件中的多个类
from entity.car import Car, ElectricCar, Battery
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

my_car = Car('Benz', 'C200L', '2024')
log.info(f'Output #1: {my_car.get_descriptive_name()}')
log.info(f'Output #1: {my_car.fill_gas_tank()}')

my_electric_car = ElectricCar('tesla', 'model 3', '2024')
log.info(f'Output #2: {my_electric_car.get_descriptive_name()}')
log.info(f'Output #2: {my_electric_car.fill_gas_tank()}')
log.info(f'Output #2: {my_electric_car.battery.describe_battery()}')
log.info(f'Output #2: {my_electric_car.get_range()}')

my_electric_car2 = ElectricCar('tesla', 'model Y', '2024')
# 将类传入类中
tesla_batery = Battery(101)
my_electric_car2.battery = tesla_batery
log.info(f'Output #3: {my_electric_car2.get_descriptive_name()}')
log.info(f'Output #3: {my_electric_car2.fill_gas_tank()}')
log.info(f'Output #3: {my_electric_car2.battery.describe_battery()}')
log.info(f'Output #3: {my_electric_car2.get_range()}')