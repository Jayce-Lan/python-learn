import logging
import logging.config
import os
from pathlib import Path
import sys

# 获取当前文件所在的目录的绝对路径，并得到其父级目录（即create_data_frame.py所在的目录）
parent_dir = Path(__file__).resolve().parent.parent
# 将父级目录添加到系统路径中
sys.path.append(str(parent_dir))
# 打印日志
current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

from create_data_frame import get_data_frame_5column, get_data_frame_only_number

######################
# 通过标签或位置修改数据
######################

df = get_data_frame_5column()
log.info(f'\n{df}')
df_numbers = get_data_frame_only_number()
log.info(f'\n{df_numbers}')

df2 = df.copy()

# DataFrame.loc[index, column] = value
df2.loc[1001, 'Name'] = 'Musk'
log.info(f'\n{df2}')

# 也可以同时修改多列
df2.loc[[1001, 1002], 'Score'] = [3, 4]
log.info(f'\n{df2}')

# 通过iloc修改
df2.iloc[1, 0] = 'Bill'
log.info(f'\n{df2}')

######################
# 通过布尔值修改数据
######################
df2 = df.copy()
df_numbers2 = df_numbers.copy()

# 匿名年龄18岁以下或者来自美国的用户
tf = (df2['Age'] < 18) | (df2['Country'] == 'USA')
df2.loc[tf, 'Name'] = 'xxx'
log.info(f'\n{df2}')

# 对于全表数字的数据，可以直接传入布尔值进行修改
df_numbers2[df_numbers2 < 400] = 0
log.info(f'\n{df_numbers2}')

# 可以通过replace替换值
# 替换全表中的值，所有列都会生效
df2 = df2.replace('USA', 'xxx')
log.info(f'\n{df2}')

# 指定只替换某一列
df2 = df2.replace({'Country': {'xxx': 'USA'}})
log.info(f'\n{df2}')

######################
# 通过设置新列设置数据
######################
df2 = df.copy()

# 批量或指定新列的值
df2.loc[:, 'discount'] = 0
df2.loc[:, 'price'] = [49.9, 5.0, 100, 100]
log.info(f'\n{df2}')

# 使用计算规则生成值
df2.loc[:, 'birth year'] = 2024 - df2['Age']
log.info(f'\n{df2}')
