import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

"""
返回简单的值
"""
def get_sum(a, b):
    return a + b;

log.info(f'Output #1: get_sum {get_sum(10, 11)}');

