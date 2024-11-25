from entity.car import Car
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

my_car = Car('Benz', 'C200L', '2024')
log.info(f'Output #1: {my_car.get_descriptive_name()}')
# 不需要在构造方法中填入公里数，而是后面另行赋值
my_car.odometer_reading = 200
log.info(f'Output #2: {my_car.read_odometer()}')
my_car.update_odometer(10)
log.info(f'Output #3: {my_car.read_odometer()}')
my_car.update_odometer(20)
log.info(f'Output #3: {my_car.read_odometer()}')
my_car.update_odometer(-30)
log.info(f'Output #3: {my_car.read_odometer()}')