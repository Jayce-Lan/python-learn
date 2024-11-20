import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 使用标识退出循环
prompt = 'Tell me something, and I will repeat it back to you.';
prompt += '\nEnter "exit" to exit.';
# 设定一个标识
run_flag = True;

message = input(prompt);
while run_flag:
    if message != 'exit':
        log.info(f'Output #2: Your entered: {message}.');
        message = input(prompt);
    else:
        log.info(f'Output #2: See you!');
        run_flag = False;