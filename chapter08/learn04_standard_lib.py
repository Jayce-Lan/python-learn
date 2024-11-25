# 导入标准库的一些方法
from random import randint, choice

import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

def get_numbers(start=1, end=6):
    """
    randint(start, end) 生成一个[start, end]的随机数
    并且循环10次打印
    """
    for i in range(10):
        log.info(f'Output #1: {i} - {randint(start, end)}')

get_numbers(0, 6)

def get_choice(list):
    """
    choice() 从列表或者元组中随机选择一个元素
    """
    log.info(f'Output #2: {choice(players)}')

# choice(sequence) 从sequence中随机选择一个元素
# sequence可以是列表或者元组
players = ['charles', 'james', 'kobe', 'eli', 'curry']
get_choice(list)

