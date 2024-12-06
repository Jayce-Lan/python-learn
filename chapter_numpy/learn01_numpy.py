import numpy as np
import math
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

"""
由于pandas是基于NumPy建立的
因此可以通过学习NumPy基本知识与概念，让学习pandas更加轻松
"""
def test_numpy1():
    array1 = np.array([1, 10, 100, 1000.])
    log.info(f'Output #1.1: {array1}')
    log.info(f'Output #1.2: {array1.dtype}') # float64
    log.info(f'Output #1.3: {array1[1]}') # float64

# test_numpy1()

def test_numpy2():
    """
    向量化和广播化
    """
    # 使用嵌套创建一个二维数组
    array1 = np.array([10, 100, 1000.])
    array2 = np.array([[1., 2., 3.],
                       [4., 5., 6.]])
    log.info(f'Output #2.1: {array2[1][1]}')
    log.info(f'Output #2.2: {array2 * array2}')
    log.info(f'Output #2.3: {array2 * array1}')
    log.info(f'Output #2.4: {array2 + 1}')
    log.info(f'Output #2.5: {array2 @ array2.T}')

# test_numpy2()

def test_numpy3():
    """
    通用函数
    通用函数不能直接作用在数组和二维数组上
    需要进行for循环
    """
    array2 = np.array([[1., 2., 3.],
                       [4., 5., 6.]])
    # math.sqrt(array2)
    array2_sqrt = np.array([[math.sqrt(i) for i in row ]for row in array2])
    log.info(f'Output #3.1: {array2}')
    log.info(f'Output #3.2: {array2_sqrt}')
    # 也可以使用numpy自带函数
    log.info(f'Output #3.3: {np.sqrt(array2)}')
    # 求每一列的和(axis = 1)为求每行的和，不填入参数为整个数组的和
    log.info(f'Output #3.4: {array2.sum(axis = 0)}')

test_numpy3()

    