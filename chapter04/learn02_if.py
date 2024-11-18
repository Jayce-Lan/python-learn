import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 简单if
age = 19;
if age >= 18:
    log.info('Output #1: You are an adult.');
    log.info('Output #1: You are old enough to vote.');
    log.info('Output #1: Are you registered to vote yet?');

# if-else
age = 17;
if age >= 18:
    log.info('Output #2: You are old enough to vote.');
    log.info('Output #2: Are you registered to vote yet?');
else:
    log.info('Output #2: You are not old enough to vote.');
    log.info('Output #2: Please registered to vote as soon as you turn 18!');

# if-elif-else
# 一旦满足，就会执行对应if模块中的代码，并跳出剩余判定
age = 18;
price = 0;
if age <= 6:
    price = 0;
elif age <= 12:
    price = 5;
elif age <= 18:
    price = 8;
else:
    price = 10;

log.info(f'Output #3.1: You will pay ${price} for the ticket.');

# 省略else
age = 68;
price = 0;
if age <= 6:
    price = 0;
elif age <= 12:
    price = 5;
elif age <= 18:
    price = 8;
elif age >= 65:
    price = 15;

log.info(f'Output #3.1: You will pay ${price} for the ticket.');

# 使用多个if来并排添加条件
# 当只需要一个条件为执行结果时，使用if-elif，当需要同时进行多个执行结果时，使用多重if
my_pizza = ['12', '$49', 'chicken'];
if '12' in my_pizza:
    log.info('Output #4.1: You have a 12-inch pizza.');
if '$69' in my_pizza:
    log.info('Output #4.2: You have only need to pay $59.99 for the ticket!');
if 'chicken' in my_pizza:
    log.info('Output #4.3: You have a chicken pizza.');
