from pathlib import Path
import json
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

def write_json_file(file_path, json_msg):
    """
    @param file_path: 写入文件地址
    @param json_msg: 要写入的json数据
    @return:
    使用json.dumps将内容写入到json文件当中
    """
    path = Path(file_path);
    content = json.dumps(json_msg);
    try:
        path.write_text(content, encoding='utf-8')
    except FileNotFoundError as exception:
        log.error(f'File not found: {exception}')
    else:
        log.info(f'Successfully write to json file: {file_path}')

def read_json_file(file_path):
    """
    @param file_path: 文件地址
    @return:
    通过json.loads读取json返回数据
    """
    path = Path(file_path)
    try:
        content = path.read_text(encoding='utf-8')
        json_data = json.loads(content)
    except FileNotFoundError as exception:
        log.error(f'File not found: {exception}')
        return None
    except json.JSONDecodeError as exception:
        log.error(f'Failed to decode JSON: {exception}')
        return None
    else:
        return json_data

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# write_json_file('/Users/lanjiesi/Documents/test/number1.json', numbers)
# log.info(read_json_file('/Users/lanjiesi/Documents/test/number1.json'))

def user_login(file_path):
    """
    @param file_path: 文件路径
    @return:
    读取json文件，检查用户名是否存在并返回True/False
    如果存在，那么直接问候用户，如果不存在，则让用户录入姓名并且写入文件
    """
    path = Path(file_path);
    # exists文件存在-返回True，文件不存在-返回False
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        log.info(f'Welcome back, {username}')
    else:
        username = input('Please enter your name: ')
        contents = json.dumps(username)
        path.write_text(contents)
        log.info(f'We\'ll remember you when you com back, {username}')

user_login('/Users/lanjiesi/Documents/test/username.json')
