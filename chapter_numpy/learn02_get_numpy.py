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

# test_get_array()

def test_create_array():
    """使用内置函数可以方便的构造数组"""
    # 构造一个10以内的数组，并且通过reshape确定数组为2行5列
    # 值得注意的是，reshape里两数的乘积需要和arange里存储的个数一致
    array1 = np.arange(2 * 5).reshape(2, 5)
    log.info(f'Output #2.1: {array1}')

    # 使用随机数构造数组，构造两行3列的数组
    array2 = np.random.randn(2, 3)
    log.info(f'Output #2.2: {array2}')

# test_create_array()

def test_array_view():
    """
    视图和副本的操作
    与list稍有不同，如果不使用.copy()方法，而是使用[:]切片
    那么其实操作的是视图的子集，一样会改变原数组的内容
    """
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = array1[:2, :2]
    log.info(f'Output #3.1: {array2}')
    # array1会被修改
    array2[0, 0] = 100
    log.info(f'Output #3.2: {array1}')
    log.info(f'Output #3.2: {array2}')

test_array_view()

def test_array_view_copy():
    """
    使用copy不会修改原数组
    """
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = array1[:2, :2].copy()
    log.info(f'Output #3.1: {array2}')
    # array1不会被修改
    array2[0, 0] = 100
    log.info(f'Output #3.2: {array1}')
    log.info(f'Output #3.2: {array2}')

test_array_view_copy()
