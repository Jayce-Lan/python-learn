import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

"""
定义一个函数
此处使用了多段注释
"""
def greet_user():
    log.info('Hello, function!')

# 调用函数
# greet_user()

"""
有参函数
"""
def greet_user2(userName):
    log.info(f'{userName}, hello!')

# 调用有参函数
# greet_user2('Jayce')

def test_function(value1, value2):
    log.info(f'value1 = {value1}, value2 = {value2}')

# 当不做任何操作时，传入的参数顺序为默认顺序
test_function('value2', 'value1');
# 也可以指定传参，此时，每个参数就会被传入指定形参中，
test_function(value2='value2', value1='value1');
# 当传入参数个数不对时，会报异常
# test_function('value1');

"""
给定函数默认值
此时，调用这个函数只传入无默认值的参数时，另一个参数会有默认值
"""
def test_function2(value1, value2 = 'value2'):
    log.info(f'value1 = {value1}, value2 = {value2}')

test_function2('test1')
test_function2('test1', 'test2')