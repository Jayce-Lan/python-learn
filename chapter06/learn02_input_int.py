import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 调用input函数从控制台拿到的数据是字符串str类型
age = input('please enter your age: ');
# 当我们需要做一些类似数值判断时，需要先将字符串转为数字
age = int(age);

if age < 18:
    log.info('Output #1: You are too young.');
elif age >= 18:
    log.info('Output #2: You are old enough.');
elif age >= 60:
    log.info('Output #3: You are too old.');