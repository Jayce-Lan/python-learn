from pathlib import Path
import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 读取文件
# path = Path('/Users/lanjiesi/Documents/test/test.txt')
# 读取一百万位圆周率
path = Path('/Users/lanjiesi/Documents/test/PI.txt')
contents = path.read_text()
# 消除末尾空格
lines = contents.splitlines()
# 承接文件内容
pi_str = ''
for line in lines:
    pi_str += line.lstrip() 

# 只打印到小数点后50位
log.info(f'Output #1: {pi_str[:52]}...')
log.info(f'Output #1: {len(pi_str)}')

# 圆周率中是否包含生日
birthday = '951024'
if birthday in pi_str:
    log.info(f'Output #2: The birthday appears in the PI.')

