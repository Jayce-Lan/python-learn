import logging
import logging.config
import os
from pathlib import Path
import sys

# 获取当前文件所在的目录的绝对路径，并得到其父级目录（即create_data_frame.py所在的目录）
parent_dir = Path(__file__).resolve().parent.parent
# 将父级目录添加到系统路径中
sys.path.append(str(parent_dir))
# 打印日志
current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

from create_data_frame import get_data_frame_5column

######################
# 通过标签或位置修改数据
######################

df = get_data_frame_5column()
log.info(f'\n{df}')

df2 = df.copy()

# DataFrame.loc[index, column] = value
df2.loc[1001, 'Name'] = 'Musk'
log.info(f'\n{df2}')

# 也可以同时修改多列
df2.loc[[1001, 1002], 'Score'] = [3, 4]
log.info(f'\n{df2}')

# 通过iloc修改
df2.iloc[1, 0] = 'Bill'
log.info(f'\n{df2}')
