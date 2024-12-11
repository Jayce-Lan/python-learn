import logging
import logging.config
import os

from create_data_frame import get_data_frame_5column, get_data_frame_only_number

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

######################
# 使用布尔索引选择数据
######################

df = get_data_frame_5column()
log.info(f'\n{df}')

# 展示国籍为美国，且年龄在40岁以上的人员信息
tf = (df['Age'] > 40) & (df['Country'] == 'USA')
log.info(f'\n{tf}')
# 选取对应的行并展示
log.info(f'\n{df.loc[tf, :]}')
# 也可以写成以下形式，效果一致
log.info(f'\n{df[tf]}')

""" 与正常的运算符不同，在DataFrame中，逻辑关系如下
    & and
    | or
    ~ not
"""
# 在正常DataFrame中可以使用in来传入列表条件
# 但是对于Series类型，需要使用isin
tf =  ~ (df['Country'].isin(['USA', 'China']))
log.info(f'\n{tf}')
log.info(f'\n{df[tf]}')

###################################
# 使用布尔值作为参数处理纯数字DataFrame
###################################
df_number = get_data_frame_only_number()
log.info(f'\n{df_number}')

# 使用DataFrame本身进行判定
log.info(f'\n{df_number < 400}')

# 直接承接布尔判定获取对应的DataFrame
# 以下过滤的结果会过滤掉大于等于400的值，只保留小于400的值
log.info(f'\n{df_number[df_number < 400]}')

