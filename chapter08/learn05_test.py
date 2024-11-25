from random import choice
import logging
import logging.config
import os

from entity.die import Die

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

def roll_die_times(times, sides): 
    """
    调用times次掷骰子方法
    骰子的面数为sides
    """
    die_6 = Die(sides)
    for i in range(times):
        log.info(f'Output #1: {i + 1} times - {die_6.roll_die()}')

# roll_die_times(10, 6)

# 测试彩票中奖
# 选项池
all_ticket = ['1', '2', '3', '4', '5', 
              '6', '7', '8', '9', '10', 
              'A', 'B', 'C', 'D', 'E']
# 中奖字母
winning_numbers = ['1', '2', 'A', 'B']

def is_winning(ticket, winning_numbers):
    my_ticket = []
    for i in range(4):
        item = choice(ticket)
        my_ticket.append(item)
        ticket.remove(item)
    
    for item in my_ticket:
        if item in winning_numbers:
            winning_numbers.remove(item)
    
    return len(winning_numbers) == 0

my_count = 1

while True:
    winning_flag = is_winning(all_ticket[:], winning_numbers[:])
    if winning_flag:
        log.info(f'Output #2: You win the lottery! uese times {my_count}')
        break
    my_count += 1