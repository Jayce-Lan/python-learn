import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 使用continue跳出当前循环
current_number = 0;
while current_number < 10:
    current_number += 1;
    if current_number % 2 == 0:
        continue;
    log.info(f'Output #1: Current number is {current_number}.');