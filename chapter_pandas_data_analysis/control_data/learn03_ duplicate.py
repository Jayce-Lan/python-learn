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

from create_data_frame import get_data_frame_5column, get_data_frame_column_duplicate

######################
# 重复数据
######################
df = get_data_frame_5column()
df_duplicate = get_data_frame_column_duplicate()
log.info(f'\n{df}')
log.info(f'\n{df_duplicate}')

"""
    可以使用drop_duplicates删除重复数据
    该方法不改变被操作的DataFrame，因此需要一个参数来承接
    若不指定列，则会对所有列进行去重
    如果指定，那么只会对某一列去重，函数会保留第一次出现的数据
"""
# 整行去重
df_drop_duplicates = df_duplicate.drop_duplicates()
log.info(f'\n{df_drop_duplicates}')

# 多列去重
df_drop_duplicates_column = df_duplicate.drop_duplicates(['Country', 'Continent'])
log.info(f'\n{df_drop_duplicates_column}')

# 单列去重
df_drop_duplicates_single_column = df_duplicate.drop_duplicates('Name')
log.info(f'\n{df_drop_duplicates_single_column}')

"""
    使用is_unique判定是否存在重复
    返回结果为False或True，当返回False时存在重复

    使用unique()获取去重后的列数据
    改方法返回一个NumPy
"""
# 判定是否重复
log.info(df['Name'].is_unique)
log.info(df['Country'].is_unique)

# 获取去重后的列信息
log.info(f'\n{df['Country'].unique()}')

"""
    使用duplicated()方法判定哪些内容是重复的
    首次出现的数据会被判定为非重复，也就是False，到后面的重复数据才会判定为True
    当传入参数keep=False时，所有重复数据都会标记为True（包括首次）
"""

log.info(f'\n{df['Country'].duplicated()}')

# 不声明列时整行匹配
log.info(f'\n{df_duplicate.duplicated()}')

# 使用keep=False参数
log.info(f'\n{df['Country'].duplicated(keep=False)}')
log.info(f'\n{df_duplicate.duplicated(keep=False)}')

# 利用keep=False的特性找出所有的重复项
# df_duplicate_duplicated = df_duplicate[df_duplicate['Country'].duplicated(keep=False)]
# 效果一致
df_duplicate_duplicated = df_duplicate.loc[df_duplicate['Country'].duplicated(keep=False), :]
log.info(f'\n{df_duplicate_duplicated}')
