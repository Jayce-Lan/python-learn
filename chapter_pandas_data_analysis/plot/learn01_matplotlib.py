import logging
import logging.config
import os
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

df = pd.DataFrame(data = np.random.rand(4, 4) * 100000,
                  index=['Q1', 'Q2', 'Q3', 'Q4'],
                  columns=['East', 'West', 'North', 'South'])
df.index.name = 'Quarters'
df.columns.name = 'Region'

log.info(f'df\n{df}')


"""
    绘图方式
    line 折线图，使用df.plot()时默认
    bar 柱状图
    barh 水平柱状图
    hist 矩形图
    box 箱线图
    kde 密度图（可以通过density启用）
    area 面积图
    scatter 散点图
    hexbin 六边形图
    pie 饼状图
"""
# 使用饼状图展示数据
# df.plot(kind='pie', subplots=True, figsize=(16, 8))
# 使用折线图绘图()默认
# df.plot()
df.plot(kind='bar')
plt.show()
