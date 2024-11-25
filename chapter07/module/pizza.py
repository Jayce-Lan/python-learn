import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

def make_pizza(size, *toppings):
    """
    在这里，第一个参数会传入size，而后面的参数才是配料
    """
    log.info(f'Output #function 1: Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        log.info(f'Output #function 1: Adding {topping} to the pizza')