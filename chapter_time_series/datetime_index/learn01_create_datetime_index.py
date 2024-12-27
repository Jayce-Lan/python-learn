import logging
import logging.config
import os

import pandas as pd
import numpy as np

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

########################
# 创建DatetimeIndex
########################
"""
pandas 为构造 DatetimeIndex 提供了 date_range 函数
它会接受一个开始日期，一个频率参数，以及周期数或者结束日期
"""

# 通过起始时间戳，创建DatetimeIndex
# 2024-12-20为开始时间
# periods=4为时间周期为4天（包括2024-12-20本身）
# 周期数和频率（'D'=daily）即每天，
daily_index = pd.date_range('2024-12-20', periods=4, freq='D')
log.info(daily_index)

# 通过起始/结束时间戳创建DatetimeIndex
# 频率设置为每周日（W-SUN）
weekly_index = pd.date_range('2024-12-01', '2024-12-31', freq='W-SUN')
log.info(weekly_index)

# 只在收入开放的博物馆有客人次
df_weekly_index = pd.DataFrame(data = [21, 14, 28, 30, 31],
                               columns=['visitors'], index=weekly_index)
log.info(f'df_weekly_index\n{df_weekly_index}')
