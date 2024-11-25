from entity.dog import *
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

my_dog = Dog('Willite', 6)
log.info(f'Output #1: my dog\'s name is {my_dog.name}, it\'s {my_dog.age} years old')
log.info(f'Output #1: {my_dog.sit()}')
log.info(f'Output #1: {my_dog.roll_over()}')

your_dog = Dog('Lucy', 8)
log.info(f'Output #2: your dog\'s name is {your_dog.name}, it\'s {your_dog.age} years old')
log.info(f'Output #2: {your_dog.sit()}')
log.info(f'Output #2: {your_dog.roll_over()}')