import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 使用input来实现用户输入交互
# input函数会将控制台录入信息赋值给变量，随后可以处理这个变量
# user_name = input('Please enter your username:');

# 多行提示的录入
message = f'Welcome to {current_filename}.py';
message += '\nPlease enter your username: '
user_name = input(message);
log.info(f'Output #1: Hello, {user_name}!');