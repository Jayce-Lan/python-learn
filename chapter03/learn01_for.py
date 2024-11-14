import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 使用for循环list
# 只有需要进行循环的部分代码需要缩进，其余均不进行缩进
cars = ['benz', 'bmw', 'audi', 'toyota'];
for item in cars: 
    log.info(f"Output #1: {item}");
    log.info('\tthis is for in\n');

log.info('do successfully!');