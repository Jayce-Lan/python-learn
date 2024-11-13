import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0]
# 加载日志配置文件
logging.config.fileConfig('logging.conf')
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename)

# 列表 list 是由一系列按特定顺序排列元素组成
bicycle = ['trek', 'cannondale', 'redline', 'specialized'];
log.info(f"Output #1: {bicycle}");

# 访问列表元素
log.info(f"Output #2: {bicycle[0].title()}");