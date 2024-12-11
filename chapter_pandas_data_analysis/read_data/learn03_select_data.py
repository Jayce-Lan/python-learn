import logging
import logging.config
import os
from pathlib import Path
import sys

# 获取当前文件所在的目录的绝对路径，并得到其父级目录（即create_data_frame.py所在的目录）
parent_dir = Path(__file__).resolve().parent.parent
# 将父级目录添加到系统路径中
sys.path.append(str(parent_dir))

from create_data_frame import get_data_frame_5column

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

######################
# 选择数据
######################

df = get_data_frame_5column()
log.info(f'\n{df}')

###############################
# DataFrame.loc[index, column]
###############################

# 单个值，行和列都用标量选择，返回值也为标量
log.info(df.loc[1001, 'Name'])

# 只用标量选择行或列，返回值是Series
log.info(f'\n{df.loc[[1001, 1003], 'Name']}')
log.info(f'\n{df.loc[1002, ['Name', 'Age']]}')

# 选取多行或多列，返回值是DataFrame
# 与list的切片不同，DataFrame的切片[start, end]包含end
log.info(f'\n{df.loc[:1003, ['Name', 'Age']]}')
log.info(f'\n{df.loc[[1001, 1003], ['Name', 'Age']]}')
log.info(f'\n{df.loc[1001 : 1003, ['Name', 'Age']]}')

# 选列的捷径
# pandas中，loc[:, colnum_name]的用法和dataframe[colnum_name]作用是一致的
log.info(f'\n{df['Name']}')
log.info(f'\n{df.loc[:, 'Name']}')

# 同理，使用loc[:, [colnum_name1, colnum_name2]]和dataframe[[colnum_name1, colnum_name2]]作用一致
log.info(f'\n{df[['Name', 'Age']]}')
log.info(f'\n{df.loc[:, ['Name', 'Age']]}')

###############################
# DataFrame.iloc[row_index, col_index]
###############################
log.info(f'\n{df}')
# 单个值，返回标量
log.info(df.iloc[0, 0])

# 单列或单行，返回Series
log.info(f'\n{df.iloc[[0, 2], 0]}')
log.info(f'\n{df.iloc[0, :]}')

# 多行
log.info(df.iloc[:3, :])
log.info(df.iloc[[1, 3], :])

