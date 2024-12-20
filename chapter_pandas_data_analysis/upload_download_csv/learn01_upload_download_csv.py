import logging
import logging.config
import os

import pandas as pd

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

"""
    导入和导出DataFrame

    数据格式/系统   导入：pandas（pd）函数   导出：DataFrame（df）方法
    CSV            pd.read_csv()             df.to_csv()
    JSON           pd.read_json()            df.to_json()
    HTML           pd.read_html()            df.to_html()
    剪切板          pd.read_clipboard()       df.to_clipboard()
    Excel          pd.read_excel()           df.to_excel()
    SQL            pd.read_sql()             df.to_sql()
"""

# 导入csv
df_read = pd.read_csv('/Users/lanjiesi/Documents/MyProject/GitProject/python-for-excel/csv/MSFT.csv')
# log.info(f'df_read\n{df_read}')
df_read.info()

# 导出csv
data = [['Oranges', 'North', 12.30],
        ['Apples', 'South', 10.55],
        ['Oranges', 'South', 22.00],
        ['Bananas', 'South', 5.90],
        ['Bananas', 'North', 31.30],
        ['Oranges', 'North', 13.10]]

df = pd.DataFrame(data, columns=['Fruit', 'Region', 'Revenue'], index=list(range(1, len(data) + 1)))

# 不指定目录的前提下，会以当前文件所在根目录为基准，生成data.csv
# df.to_csv('data.csv')
