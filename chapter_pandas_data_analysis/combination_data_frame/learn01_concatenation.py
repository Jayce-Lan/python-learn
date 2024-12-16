import logging
import logging.config
import os

import pandas as pd
from create_data_frame import get_data_frame_user2, get_data_frame_user4, get_more_categories

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

df = get_data_frame_user4()
more_users = get_data_frame_user2()
categories_df = get_more_categories()
log.info(f'\n{df}')
log.info(f'\n{more_users}')
log.info(f'\n{categories_df}')

######################
# 连接
######################

"""
    使用concat方法，可以让DataFrame自动识别列或者行进行连接
    多个DataFrame会连接到一起，通过设置axis参数决定是行连接还是列连接
    而参数的匹配交由pandas进行自动判断
    当设置行链接时，会自动匹配相同的列进行数据插入（添加）；当然，这有可能会出现重复索引
    当设置列连接时，会自动匹配索引进行列插入（新增）
    concat支持多个DataFrame，只需要插入到数组参数中即可
"""
 
# 设置axis=0按行连接
df_concat = pd.concat([df, more_users], axis=0)
log.info(f'\n{df_concat}')

# 设置axis=1按列连接（通过索引匹配）
df_concat = pd.concat([df, categories_df], axis=1)
log.info(f'\n{df_concat}')
