from pathlib import Path
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

def catch_exception1():
    """
    使用try-except捕获异常
    """
    try:
        log.info(5 / 0)
    except ZeroDivisionError as e:
        log.error(f'Caught division by zero: {e}')

# catch_exception1()

def test_input():
    """
    使用else去执行异常以外的代码块
    如果在try中的代码没被except补货，则执行else模块的代码
    当try判定无异常后才要执行的代码都应当放入else当中
    """
    while True:
        number1 = input('please enter a number-1(input \'q\' to exit.):')
        if number1.lower() == 'q':
            break
        number2 = input('please enter a number-2(input \'q\' to exit.):')
        if number2.lower() == 'q':
            break
        # try-except-else
        try:
            answer = int(number1) / int(number2)
        except ZeroDivisionError as e:
            log.error(f'Caught division by zero...{e}, dont enter number-2 by 0!')
        else:
            log.info(f'The {number1} / {number2} = {answer}')

# test_input()

def catch_exception2(file_path):
    """
    捕获文件异常
    当获取到一个找不到的路径时，捕获异常
    """
    path = Path(file_path)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError as e:
        log.error(f'file path not found: {e}')
    else:
        # 计算文本大致的单词数
        words = contents.split()
        words_count = len(words)
        log.info(f'Total number of words in the file: {words_count}')

# catch_exception2('/Users/lanjiesi/Documents/test/test.txt')

def pass_exception(file_path):
    """
    静默异常
    有时候执行程序并不需要告知用户是否存在异常
    此时在except当中执行pass，会让python跳过异常继续执行
    """
    path = Path(file_path)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # 计算文本大致的单词数
        words = contents.split()
        words_count = len(words)
        log.info(f'Total number of words in the \'{file_path}\': {words_count}')

# 由于静默原因，在找不到文件的情况下不会报出异常
# file_paths = ['/Users/lanjiesi/Documents/test/test.txt', 
#               '/Users/lanjiesi/Documents/test/test_write.txt', 
#               '/Users/lanjiesi/Documents/test/test2.txt']
# for file_path in file_paths:
#     pass_exception(file_path)
