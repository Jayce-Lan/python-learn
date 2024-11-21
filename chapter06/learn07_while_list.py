import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 使用while循环判定条件的特性可以进行数组移动
# 创建一个未认证的数组
unconfirmed_user = ['Alice', 'Bob', 'Tony'];
# 创建一个已认证的数组，数组为空
confirmed_users = [];

# 使用while循环模拟用户认证，认证后从未认证数组移动到认证用户中
while unconfirmed_user:
    # 记录从未认证中移除的用户用于放入已认证列表中
    current_user = unconfirmed_user.pop();
    log.info(f'Output #1: {current_user} has been confirmed.');
    confirmed_users.append(current_user);

# 打印已认证的用户列表
log.info(f'Output #1.1: {unconfirmed_user}');
log.info(f'Output #1.2: {confirmed_users}');

# 删除数组中存在的某个元素
pets = ['dog', 'cat', 'dog', 'rabbit', 'goldfish', 'cat', 'dog'];
log.info(f'Output #2.1: {pets}');

# 由于remove函数只会删除第一个数组元素，因此可以使用while的特性做这个处理
while 'dog' in pets:
    pets.remove('dog');

log.info(f'Output #2.2: {pets}');