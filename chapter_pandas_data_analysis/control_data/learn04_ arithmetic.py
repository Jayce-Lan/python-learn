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
# 算数运算
######################
df = get_data_frame_only_number()
log.info(f'\n{df}')

"""
    向量化技术可以简单的让整个DataFrame都做同一个操作
    这并不会改变原始的DataFrame
"""
log.info(f'\n{df + 100}')
log.info(f'\n{df - 200}')
log.info(f'\n{df * 2}')
log.info(f'\n{df / 2}')

"""
    数据对齐（data alignment）
    当对多个DataFrame使用算数运算符时，pandas会自动将它们按照索引和列对齐
    这相当于求多个DataFrame的并集然后再进行运算
"""
# 创建一个索引从1开始，只有city1和city4的DataFrame
df_index_start_2 = pd.DataFrame(data = [[100, 200], 
                                        [300, 400]],
                                        columns = ['city1', 'city4'],
                                        index = [1, 2])
log.info(f'\n{df_index_start_2}')

# 当两个DataFrame相互做运算时，由于数据对齐操作
# 只会有index为1的city1列有数据，其余均为NaN
sum_df = df + df_index_start_2
log.info(f'\n{sum_df}')

"""
    如果不希望数据为NaN而是0，那么需要使用方法进行处理
    并传入参数fill_value = 0
    这会让只有某一个DataFrame有的数据转为0
    但是如果DataFrame都没有的列，还是将以NaN展示
    ------------------
    方法    对应运算符
    add      +
    sub      -
    mul      *
    div      /
    pow      **
"""
sum_df = df.add(df_index_start_2, fill_value=0)
log.info(f'\n{sum_df}')

"""
    广播机制
    当操作DataFrame和Series时，默认按照index索引广播
    当Series为列时，需要使用add方法，并传入axis=0参数声明行广播
    也就是每行按照列对应的索引进行操作
"""
add_series = df + df.loc[1, :]
log.info(f'\n{add_series}')

# 此处为，index为0和1的行各自增加了city1的值；
add_series = df.add(df.loc[:, 'city1'], axis = 0)
log.info(f'\n{add_series}')
