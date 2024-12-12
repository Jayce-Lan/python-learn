import logging
import logging.config
import os
from pathlib import Path
import sys
import pandas as pd

# 获取当前文件所在的目录的绝对路径，并得到其父级目录（即create_data_frame.py所在的目录）
parent_dir = Path(__file__).resolve().parent.parent
# 将父级目录添加到系统路径中
sys.path.append(str(parent_dir))
# 打印日志
current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

from create_data_frame import get_data_frame_only_number

######################
# 应用函数
######################

"""
    pandas提供了一个applymap方法
    里面允许传入函数，一般为单参数函数，用于处理DataFrame中的数据
    也可以传入lambda表达式直接构建一个函数
"""

df = get_data_frame_only_number()
log.info(f'\n{df}')

def square(x):
    return x ** 2

# 所有的参数都会调用square函数
square_df = df.applymap(square)
log.info(f'\n{square_df}')

# 也可以使用lambda表达式
# 此处其实相当于声明一个参数为x的函数，return一个x*2的值
lambda_df = df.applymap(lambda x: x * 2)
log.info(f'\n{lambda_df}')
