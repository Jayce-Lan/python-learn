import numpy as np
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

"""
获取数组中的元素
"""
ARRAY = np.array([10, 100, 1000.])
ARRAY2 = np.array([[1, 2, 3], 
                   [4, 5., 6]])

def test_get_array():
    log.info(f'Output #1.1: {ARRAY[1]}')
    log.info(f'Output #1.2: {ARRAY2[1][1]}')
    log.info(f'Output #1.3: {ARRAY2[1, 1]}')
    log.info(f'Output #1.3: {ARRAY2[:, :]}')
    log.info(f'Output #1.3: {ARRAY2[:, :1]}')

test_get_array()