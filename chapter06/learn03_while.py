import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# current_number = 1;

# while current_number <= 5:
#     log.info(f'Output #1: Current number is {current_number}.');
#     current_number += 1;

# 设定“exit”为程序退出的函数，用户录入其他字符均打印
prompt = 'Tell me something, and I will repeat it back to you.';
prompt += '\nEnter "exit" to exit.';

message = input(prompt);
while message != 'exit':
    log.info(f'Output #2: Your entered: {message}.');
    message = input(prompt);