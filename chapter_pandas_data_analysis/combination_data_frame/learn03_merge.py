import logging
import logging.config
import os

import pandas as pd

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

# 两个DataFrame拥有一个列名为category的列
df1 = pd.DataFrame(data = [[1, 2, 'a'], [3, 4, 'c'], [5, 6, 'b']],
                   columns = ['A', 'B', 'category'])
df2 = pd.DataFrame(data = [[10, 20, 'b'], [30, 40, 'c']],
                   columns = ['C', 'D', 'category'])
log.info(f'df1\n{df1}')
log.info(f'df2\n{df2}')

######################
# 两个DataFrame连接-merge
######################

"""
    与concat不同，join和merge只能操作两个DataFrame
    merge不依赖索引进行连接，而是依赖DataFrame中的一列或者多列
    merge可以通过on参数提供的一列或多列作为连接条件（join condition）
    这些列必须是两个DataFrame共有的，它们会被用来进行行匹配

    merge方法可以传入“how”参数来进行连接声明
    关于连接的描述：
    inner 内连接，只保留索引为两个DataFrame共有的行
    left  左连接，左端DataFrame保留所有的行，用右端DataFrame中的行与左端匹配
    right 右连接，右端DataFrame保留所有的行，用左端DataFrame中的行与右端匹配
    outer 外连接，两个DataFrame行索引的并集

    当出现一对多的问题时，会保留匹配成功的多行
"""
# 内连接（category为b、c的行得以保留，并进行匹配）
df_inner_merge = df1.merge(df2, how='inner', on=['category'])
log.info(f'df_inner_merge\n{df_inner_merge}')

# 左连接（category为b、c的行得以保留，并进行匹配，df1中的行保留，df2中的行匹配失败的列为空值）
df_left_merge = df1.merge(df2, how='left', on=['category'])
log.info(f'df_left_merge\n{df_left_merge}')

# 右连接（category为b、c的行得以保留，并进行匹配，df2中的行保留，df1中的行匹配失败的列为空值）
df_left_merge = df1.merge(df2, how='right', on=['category'])
log.info(f'df_left_merge\n{df_left_merge}')

# 外连接（category为b、c的行得以保留，并进行匹配，df1和df2中的行索引的并集）
df_outer_merge = df1.merge(df2, how='outer', on=['category'])
log.info(f'df_outer_merge\n{df_outer_merge}')
