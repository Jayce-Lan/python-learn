import logging
import logging.config
import os
import pandas as pd

# 打印日志
current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

######################
# 处理文本列
######################

users = pd.DataFrame(data=[' musk ', ' Jim', 'Jenny', 'Tim '],
                  columns=['name'])
log.info(f'\n{users}')

# 去除文本多余的空格
users_clear = users.loc[:, 'name'].str.strip()
log.info(f'\n{users_clear}')

# 去除空格并首字母大写
users_clear_upper = users.loc[:, 'name'].str.strip().str.capitalize()
log.info(f'\n{users_clear_upper}')

# 找到所有以J开头的名字，该方法返回False或True
users_j_start = users_clear_upper.str.startswith('J')
log.info(f'\n{users_j_start}')

log.info(f'\n{users.loc[users_j_start, :]}')
