import logging
import logging.config
import os
import pandas as pd

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

def test_get_data_frame_columns():
    """
    通过列创建一个dataframe
    """
    data = {'Name': ['Mark', 'John', 'Tim', 'Jenny'],
            'Age': [55, 33, 41, 12],
            'Country': ['USA', 'USA', 'China', 'Italy'],
            'Score': [4.5, 6.7, 3.9, 9.0],
            'Continent': ['America', 'America', 'Asia', 'Europe']}
    return pd.DataFrame(data, index=[1001, 1002, 1003, 1004])

data_frame_columns = test_get_data_frame_columns()
log.info(f'\n{data_frame_columns}')

# 获取dataframe的列信息
log.info(data_frame_columns.columns)

##################################
# 列的操作
##################################

# 重命名列名
# 可以通过传入inplace=True让dataframe本身被操作
# data_frame_columns.rename(columns={'Name': 'Full Name', 'Age': 'Years Old'}, inplace=True)
df = data_frame_columns.rename(columns={'Name': 'Full Name', 'Age': 'Years Old'})
log.info(f'\n{df}')

# 删除某列
df = data_frame_columns.drop(columns=['Name', 'Continent'])
log.info(f'\n{df}')
# 删除索引
df = data_frame_columns.drop(index=[1001, 1002])
log.info(f'\n{df}')
# 删除列的同时删除索引
df = data_frame_columns.drop(columns=['Name', 'Continent'], 
                             index=[1001, 1003])
log.info(f'\n{df}')

# 获取部分列，类似于删除某些列的操作，loc[行（索引）, 列]
# 当指定列名时，只会获取dataframe中的这些列
df = data_frame_columns.loc[:, ['Name', 'Age', 'Score']]
log.info(f'\n{df}')
