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

# 索引的名称可以进行手动设置
data_frame_row.index.name = 'user_id'
log.info(f'\n{data_frame_row}')

# 如果需要将索引列变成普通的列，可以使用reset_index()
# 此时，DataFrame会自动生成一个新的索引
# 此方法需要一个新的DataFrame承接，原本的data_frame_row不会被改变
data_frame_row_reset = data_frame_row.reset_index()
log.info(f'\n{data_frame_row_reset}')



