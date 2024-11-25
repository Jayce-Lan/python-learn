from pathlib import Path
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

users = []

def add_users(users):
    """
    获取控制台输入的用户
    """
    while True:
        name = input('Please enter your name (or enter "q" to quit): ')
        if name.lower() == 'q':
            break
        users.append(name)

def write_users(users):
    """
    将用户换行写入文本中
    """
    path = Path('/Users/lanjiesi/Documents/test/test_write.txt')
    input_str = ''
    for user in users:
        input_str += (user + '\n')
    path.write_text(input_str)

add_users(users)
write_users(users)