from pathlib import Path
import json
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

# ----------------------------------------------------------------
# 针对learn04中user_login方法的重构
# 将方法拆分成各个独立的模块
# ----------------------------------------------------------------
def greet_user(file_path):
    """
    @param file_path: 文件路径
    @return:
    方法重构
    拆分方法，让每个方法专注于做自己的事
    """
    path = Path(file_path);
    username = get_stored_username(path);
    if username:
        log.info(f'Welcome back, {username}')
    else:
        username = get_new_username(path);
        log.info(f'We\'ll remember you when you com back, {username}')

def get_stored_username(path):
    """
    @param path: 获取文件内容
    @return:
    获取存储的username
    如果存在，则读取文件，并返回用户名；如果不存在，则返回None
    """
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None

def get_new_username(path):
    """
    @param path: 获取文件路径
    @return:
    获取新输入的username
    """
    username = input('Please enter your name: ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

# 实际调用当中，只需要调用greet_user即可
# greet_user('/Users/lanjiesi/Documents/test/send_json/username.json')

# ----------------------------------------------------------------
# 练习，修改上述被重构的程序，由存储字段变为存储字典
# ----------------------------------------------------------------

def greet_user_dict(file_path):
    """
    @param file_path: 文件路径
    @return:
    方法重构
    拆分方法，让每个方法专注于做自己的事
    """
    path = Path(file_path);
    user = get_stored_username_dict(path);
    # 确认当前用户是否是本人，如果不是，则调用新的插入方法插入数据
    user_flag = input(f'{user.get('username')} is your user name?(Y/N)');
    if user and user_flag.lower() == 'y':
        log.info(f'Welcome back, {user.get('username')}, your password is {user.get('password')}')
    else:
        user = get_new_username_dict(path);
        log.info(f'We\'ll remember you when you com back, {user.get('username')}, your password is {user.get('password')}')
            

def get_stored_username_dict(path):
    """
    @param path: 获取文件内容
    @return:
    获取存储的username
    如果存在，则读取文件，并返回用户名；如果不存在，则返回None
    """
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None

def get_new_username_dict(path):
    """
    @param path: 获取文件路径
    @return:
    获取新输入的user
    """
    user = {}
    username = input('Please enter your name: ')
    user['username'] = username
    password = input('Please enter your password: ')
    user['password'] = password
    contents = json.dumps(user)
    path.write_text(contents)
    return user

greet_user_dict('/Users/lanjiesi/Documents/test/send_json/user.json')
