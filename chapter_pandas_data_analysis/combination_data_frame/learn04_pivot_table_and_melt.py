import logging
import logging.config
import os

import pandas as pd

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

data = [['Oranges', 'North', 12.30],
        ['Apples', 'South', 10.55],
        ['Oranges', 'South', 22.00],
        ['Bananas', 'South', 5.90],
        ['Bananas', 'North', 31.30],
        ['Oranges', 'North', 13.10]]

sales = pd.DataFrame(data, columns=['Fruit', 'Region', 'Revenue'])
log.info(f'sales\n{sales}')

################################
# 透视和熔化
################################
"""
    使用pivot_table透视DataFrame

    要创建数据透视表，需要将DataFrame作为第一个参数传递给pivot_table函数
    index和columns分别制定了哪一列会成为数据透视表的行标签和列标签
    values会通过aggfunc（以字符串或者NumPy ufunc的形式提供）被聚合到结果DataFrame中的数据部分
    margins对应的是Excel这种的Grand Total，如果省略margins和margins_name参数，那么结果不会出现Total列
"""
# 透视表
pivot = pd.pivot_table(sales,
                       index='Fruit', columns='Region',
                       values='Revenue', aggfunc='sum',
                       margins=True, margins_name='Total')
log.info(f'pivot\n{pivot}')

"""
    使用melt透视图表

    透视数据意味着将一列（上述为Region）中不重复的值转化为数据透视表中的列标题
    然后再聚合另一列中的值。
    通过数据透视可以轻松获取感兴趣的纬度的概要信息
    在上述透视表中，一眼就能看出在北部Apples没有销售；而在南部大部分利润来源于Oranges

    如果需要将列标题转换成列的值，以便从另一个角度透视数据，可以使用melt
    严格意义上来说，melt是pivot_table的反函数（获得一个相当于未被透视的结果）

    此处获取的是 pivot.iloc[:-1, :-1] 是为了省略Total列
    value_vars定义了想要“反透视”的列
"""
melt_df = pd.melt(pivot.iloc[:-1, :-1].reset_index(),
                  id_vars='Fruit',
                  value_vars=['North', 'South'],
                  value_name='Revenue')
log.info(f'melt_df\n{melt_df}')
