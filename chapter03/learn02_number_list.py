import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 使用 range 函数
# range(start, end) 生成一个 [start, end) 的整数数组，当end小于等于start时，生成空数组
for item in range(1, 5):
    log.info(f"Output #1: {item}");

log.info('for Ouput #1 is success!');

# 当 range(end) 时，生成 [0, end) 的数组
for item in range(6):
    log.info(f"Output #2: {item}");
log.info('for Ouput #2 is success!');

# 使用 list 函数 + range 创建数值列表
log.info(f'Output #3.1: {range(6)}'); # range(0, 6)
numbers = list(range(1, 6));
log.info(f'Output #3.1: {numbers}'); # [1, 2, 3, 4, 5]

# 定制步长
# range(start, end, num) 从start开始，不断的增加 num，直至达到或超过终值 end : [start, end)
log.info(f'Output #3.2: {list(range(1, 10, 2))}') # [1, 3, 5, 7, 9]
log.info('for Ouput #3 is success!');

# 生成1-10的平方数
squares = [];
for num in range(1, 11):
    squares.append(num ** 2);
log.info(f'Output #4: {squares}') # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 数值列表的简单计算
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
log.info(f'Output #5.1: {sum(numbers)}'); # 45
log.info(f'Output #5.2: {min(numbers)}'); # 0
log.info(f'Output #5.3: {max(numbers)}'); # 9

# 列表推导式
squares2 = [item ** 2 for item in range(1, 11)];
log.info(f'Output #6: {squares2}') # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]