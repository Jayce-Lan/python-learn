import logging
import logging.config
import os

from create_data_frame import get_data_frame_5column

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

######################
# 通过MultiIndex选择数据
######################

df = get_data_frame_5column()
log.info(f'\n{df}')

"""
    MultiIndex是一种多级索引
    它可以将数据按层次分组，这样就可以更方便的访问DataFrame的子集
    这有点类似于SQL中的group by
"""
# 将df根据Continent-Country分层级添加索引
df_multi = df.reset_index().set_index(['Continent', 'Country'])
log.info(f'\n{df_multi}')

# 按Continent-Country排序
df_multi = df_multi.sort_index(ascending=False)
log.info(f'\n{df_multi}')

# 只截取某个索引的数据
log.info(f'\n{df_multi.loc['America', :]}')
