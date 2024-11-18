import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 简单事例
cars = ['benz', 'bmw', 'audi', 'honda', 'toyota'];
for car in cars:
    if car == 'bmw':
        log.info(f'Output #1: {car.upper()}');
    else:
        log.info(f'Output #1: {car.title()}');


# 条件测试
car = 'bmw';
log.info(f'Output #2.1: {car == 'bmw'}'); # True
log.info(f'Output #2.1: {car == 'benz'}'); # False

# 检查字母时忽略大小写
car = 'Benz';
log.info(f'Output #2.2: {car == "benz"}'); # False
log.info(f'Output #2.2: {car.lower() == "benz"}'); # True

# 等与不等
if car != 'bmw':
    log.info(f'Output #2.3: This is\'t bmw! This is  {car.title()}');

# 使用in判定元素是否存在列表值中
if car.lower() in cars:
    log.info(f'Output #2.4: {car} is in the list.');

# 使用not in判断元素是否不在列表中
if 'nissan' not in cars:
    log.info(f'Output #2.5: Nissan is not in the list.');