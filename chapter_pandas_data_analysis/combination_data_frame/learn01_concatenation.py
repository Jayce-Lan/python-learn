import logging
import logging.config
import os
from create_data_frame import get_data_frame_user2, get_data_frame_user4

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

df = get_data_frame_user4()
more_users = get_data_frame_user2()
log.info(f'\n{df}')
log.info(f'\n{more_users}')

######################
# 连接
######################


