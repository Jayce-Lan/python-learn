import logging
import logging.config
import os

import pandas as pd

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

# 默认index为0,1,2
df1 = pd.DataFrame(data = [[1, 2], [3, 4], [5, 6]],
                   columns = ['A', 'B'])
# 声明index为1,3
df2 = pd.DataFrame(data = [[10, 20], [30, 40]],
                   columns = ['C', 'D'],
                   index = [1, 3])
log.info(f'df1\n{df1}')
log.info(f'df2\n{df2}')

######################
# 两个DataFrame连接-join
######################

"""
    与concat不同，join和merge只能操作两个DataFrame
    join方法依赖的是索引进行连接
    join方法可以传入“how”参数来进行连接声明
    关于连接的描述：
    inner 内连接，只保留索引为两个DataFrame共有的行
    left  左连接，左端DataFrame保留所有的行，用右端DataFrame中的行与左端匹配
    right 右连接，右端DataFrame保留所有的行，用左端DataFrame中的行与右端匹配
    outer 外连接，两个DataFrame行索引的并集
"""
# 内连接（只会保留索引为1的行）
df_inner_join = df1.join(df2, how='inner')
log.info(f'df_inner_join\n{df_inner_join}')

# 左连接（保留df1所有行，df2与之匹配，匹配失败的列为空值）
df_left_join = df1.join(df2, how='left')
log.info(f'df_left_join\n{df_left_join}')

# 右连接（保留df2所有行，df1与之匹配，匹配失败的列为空值）
df_right_join = df1.join(df2, how='right')
log.info(f'df_right_join\n{df_right_join}')

# 外连接（保留df1和df2所有行，匹配成功的列的值，匹配失败的列为空值）
df_outer_join = df1.join(df2, how='outer')
log.info(f'df_outer_join\n{df_outer_join}')
