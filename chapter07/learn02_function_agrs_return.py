import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

"""
返回简单的值
"""
def get_sum(a, b):
    return a + b;

# log.info(f'Output #1: get_sum {get_sum(10, 11)}');

"""
让实参可选
每个人都有姓氏和名字，有部分人会有中间名，但是不是全部
因此默认中间名为空字符串，使得方法适配所有姓名
"""
def greet_user(frist_name, last_name, middle_name = ''):
    log.info(f'Output #2: {frist_name} {middle_name} {last_name}, hello!');

# greet_user('John', 'Doe');
# greet_user('Jane', 'Smith', 'Elizabeth');

# 返回字典
"""
使用赋值None的特性，None在if判定中相当于false
如果没有该属性就不放入字典中
"""
def get_user_info(user_name, first_name, last_name, age = None):
    user = {'user_name': user_name, 'first_name': first_name, 'last_name': last_name};
    if age:
        user['age'] = age;
    return user;

# user_info = get_user_info('Jayce', 'Jayce', 'Lan', 30);
# log.info(f'Output #3: {user_info}');
# user_info = get_user_info('Musk', 'Elon', 'Musk');
# log.info(f'Output #3: {user_info}');

# 使用while循环与输入，通过调用函数进行录入
def get_user(fristName, lastName):
    log.info(f'Hello, {fristName} {lastName}!')

def get_message(firstOrLats):
    return f'please input your {firstOrLats} name:'

while True:
    message = get_message('frist name')
    message += '\n(input \'q\' to exit)'
    frist_name = input(message)
    if frist_name.lower() == 'q':
        log.info('See you!')
        break
    
    message = get_message('last name')
    message += '\n(input \'q\' to exit)'
    last_name = input(message)
    if last_name.lower() == 'q':
        log.info('See you!')
        break
    get_user(frist_name, last_name)
