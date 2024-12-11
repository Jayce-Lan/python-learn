import logging
import logging.config
import os

import pandas as pd

"""
xlsx的文件读取除了明显要引入pandas依赖以外，还需要自行安装openpyxl依赖
"""

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

def test_read_excel_by_pandas(file_path:str):
    """
    @param file_path: 文件路径
    @return: pandas DataFrame
    读取Excel表格并返回DataFrame
    """
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        log.error(f'Error reading Excel file: {e}')

# file_path = '/Users/lanjiesi/Documents/test/test_pandas/测试表格1.xlsx'
# log.info(f'\n{test_read_excel_by_pandas(file_path)}')

def test_get_data_frame_by_row():
    """按行创建一个DataFrame"""
    data = [['Mark', 55, 'USA', 4.5, 'America'],
            ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'China', 3.9, 'Asia'],
            ['Jenny', 12, 'Italy', 9.0, 'Europe']]
    # 索引并非必要创建，如果不指定索引，那么将会自动生成一个从0开始的索引
    # 由于可以自行设置的原因，DataFrame的索引可以重复，但是会影响查询效率
    df = pd.DataFrame(data, 
                      columns=['Name', 'Age', 'Country', 'Score', 'Continent'],
                      index=[1001, 1002, 1003, 1004])
    # df = pd.DataFrame(data, 
    #                   columns=['Name', 'Age', 'Country', 'Score', 'Continent'])
    return df

data_frame_row = test_get_data_frame_by_row()
log.info(f'\n{data_frame_row}')


################################
# 索引的操作
################################

# 索引的名称可以进行手动设置
data_frame_row.index.name = 'user_id'
log.info(f'\n{data_frame_row}')

# 如果需要将索引列变成普通的列，可以使用reset_index()
# 此时，DataFrame会自动生成一个新的索引
# 此方法需要一个新的DataFrame承接，原本的data_frame_row不会被改变
data_frame_row_reset = data_frame_row.reset_index()

# 也可以通过set_index('col_name')设置新的索引
# 原本的data_frame_row不会被改变
data_frame_row_reset = data_frame_row.reset_index().set_index('Name')
log.info(f'\n{data_frame_row_reset}')
log.info(f'\n{data_frame_row}')

# 可以通过reindex(index_list)的方法批量更换索引
# 但是这只会接管所有能匹配索引的行，匹配不到的会引入含有空值NaN的行
# 被忽略的索引对应的行将会被丢弃，例如下面的例子只会匹配到 1001、1002
data_frame_row_reset = data_frame_row.reindex([999, 1001, 1002, 1005])
log.info(f'\n{data_frame_row_reset}')
log.info(f'\n{data_frame_row}')

################################
# DataFrame的方法
################################

# DataFrame的方法返回的都是副本，不直接修改原本的DataFrame

# 根据索引对DataFrame进行排序
df = data_frame_row.sort_index()
log.info(f'\n{df}')

# 可以使用sort_values()对列进行排序

# 单列排序，默认升序排列
df = data_frame_row.sort_values('Name')
log.info(f'\n{df}')
# 传入ascending = False参数进行降序排列
df = data_frame_row.sort_values('Name', ascending = False)
log.info(f'\n{df}')

# 多列排序，默认升序排列
df = data_frame_row.sort_values(['Country', 'Score'])
log.info(f'\n{df}')
# 传入ascending = False参数进行降序排列
# 或者传入ascending = [False, True] 进行首列降序，第二列升序的排列
df = data_frame_row.sort_values(['Country', 'Score'], ascending = [False, True])
log.info(f'\n{df}')
df = data_frame_row.sort_values(['Country', 'Score'], ascending = False)
log.info(f'\n{df}')