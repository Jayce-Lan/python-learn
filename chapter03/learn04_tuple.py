import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 元组
# 与数组不同，数组是可以进行修改的（crud），但是元组是无法进行修改的，类似Java中的final
# 元组的声明方式是 (value1, value2, ...)
tuple1 = (100, 200);
log.info(f'Output #1.1: {tuple1}');
log.info(f'Output #1.2: {tuple1[0]}');
log.info(f'Output #1.3: {tuple1[1]}');

# 元组的修改是不被允许的
# tuple1[0] = 200; # 发生报错

# 元组是由逗号标识的，圆括号只是让元组看起来更加简洁清晰
# 如果需要定义一个单元素的元组，那么需要有逗号进行结尾
tuple2 = (100,);
log.info(f'Output #2.1: {tuple2}'); # (100,)
log.info(f'Output #2.2: {tuple2[0]}'); # 100

# 遍历元组
for item in tuple1:
    log.info(f'Output #3: {item}');

# 通过重新赋值修改元组变量
log.info('Output #4.1: modified output');
tuple1 = (300, 400);
for item in tuple1:
    log.info(f'Output #4.2: {item}');

