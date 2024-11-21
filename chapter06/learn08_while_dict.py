import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 利用while的特性模拟用户调查，将调查结果放入字典中
responses = {}
polling_active = True

while polling_active:
    # 提示输入姓名和被调查的回答
    name = input('\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')

    # 将答案存入字典
    responses[name] = response

    # 询问是否还有其他人参与调查
    repeat = input('Would you like to let another person respond? (y/n)')
    if repeat.lower() == 'n':
        polling_active = False

log.info(responses)
# 输入运行结果
for name, response in responses.items():
    log.info(f'{name} would like to climb {response}')