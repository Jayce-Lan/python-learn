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
# 缺失数据（空值）
######################
df = get_data_frame_5column()
log.info(f'\n{df}')

df2 = df.copy()

"""
    空值，即None，类似Java和SQL中的null
    对应Excel中的“ #N/A ”
    设置时，都为None，但是当数据展示时，数值类型会被变为NaN，即Not-a-Number
    这对应NumPy中的np,nan
    对于时间类型，则是pd.NaT
    因此在统一设置时可以直接使用None
"""
# 手动设置几个空值
df2.loc[1001, 'Score'] = None
df2.loc[1003, :] = None
log.info(f'\n{df2}')

"""
    dropna() 可以移除有空值的行
    该方法不改变被操作的DataFrame，因此需要一个参数来承接
    当方法不传入任何参数时，移除某一列有空值的行；
    可以使用how = 'all' 处理整行为空值的行
"""
# dropna()移除所有包含缺失数据的行
df2_dropna = df2.dropna()
log.info(f'\n{df2_dropna}')
log.info(f'\n{df2}')

# dropna() 移除整行为空值的行
df2_dropna_all = df2.dropna(how='all')
log.info(f'\n{df2_dropna_all}')
log.info(f'\n{df2}')

# 使用isna判定整个DataFrame或Series某个位置是否为空值，为空返回True
df2_isna = df2.isna()
log.info(f'\n{df2_isna}')

# 使用fillna填补空值
# 此处为将Score列补齐为平均数
df2_fillna = df2.fillna({'Score': df2['Score'].mean()})
log.info(f'\n{df2_fillna}')
