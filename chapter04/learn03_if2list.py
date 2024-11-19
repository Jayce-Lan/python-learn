import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 使用if处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'];
for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers':
        log.info('Output #1.1: Sorry, we are out of green peppers right now.');
    else:
        log.info(f'Output #1.1: Adding {requested_topping}');

log.info('Output #1.2: Finished making pizza!');

# list判空
# 对于数值0、控制None、单引号/双引号空字符串''/""、空列表[]、空元组()、空字典{}，python都回返回False
requested_toppings = [];
if requested_toppings:
    for requested_topping in requested_toppings:
        log.info(f'Output #2: Adding {requested_topping}');
else:
    log.info('Output #2: No toppings were added.');

num1 = 0
if num1: 
    log.info('Output #2.1: Number is non-zero.');
else:
    log.info('Output #2.1: Number is zero.');

# 使用多个列表
# 配料表，厨房现有的配料
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese'];
# 点单信息，存储用户点单
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'];

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        log.info(f'Output #3.1: Adding {requested_topping}');
    else:
        log.info(f'Output #3.1: Sorry, we don\'t have {requested_topping}.');
log.info('Output #3.2: Finished making pizza!');
