import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 使用 list[start : end] 做list切片
# start 开始下标，end 结束下标，截取 [start, end) 区间内的数组下标的元素
players = ['charles', 'james', 'kobe', 'eli', 'curry'];
log.info(f'Output #1.1: {players[0 : 3]}'); # ['charles', 'james', 'kobe']
log.info(f'Output #1.2: {players[1 : 4]}'); # ['james', 'kobe', 'eli']
# 该操作不变更原本list
log.info(f'Output #1.3: {players}'); # ['charles', 'james', 'kobe', 'eli', 'curry']

# start为空，则默认从0开始
log.info(f'Output #1.4: {players[:4]}'); # ['charles', 'james', 'kobe', 'eli']
# end为空，则默认遍历到最后一个
log.info(f'Output #1.5: {players[2:]}'); # ['kobe', 'eli', 'curry']
# 如果end为空，且start为负数，则打印list的最后aug(start)位
log.info(f'Output #1.6: {players[-2:]}'); # ['eli', 'curry']

# 遍历切片
# 指定了切片后，不会遍历整个players，只会遍历切片结果
for item in players[1 : 4]:
    log.info(f'Output #2.1: {item}');


# 复制列表

# list[:] 进行深拷贝
# 使用上述方法，如果start与end均为空，那么将会完全复制这个list，利用这个特性可以复制列表
copied_players = players[:];
log.info(f'Output #3.1: {players}') # ['charles', 'james', 'kobe', 'eli', 'curry']
log.info(f'Output #3.2: {copied_players}') # ['charles', 'james', 'kobe', 'eli', 'curry']

# 复制结束后，可以在自己的列表中加入一些新的属性，这不会改变原列表
# list被复制后，改变原列表的内容，也不会影响到复制list的内容
my_list1 = ['a', 'b', 'c', 'd', 'e'];
copy_my_list1 = my_list1[:];
log.info(f'Output #3.3: {my_list1}'); # ['a', 'b', 'c', 'd', 'e']
log.info(f'Output #3.4: {copy_my_list1}'); # ['a', 'b', 'c', 'd', 'e']
my_list1.append("g");
copy_my_list1.append('f');
log.info(f'Output #3.5: {my_list1}'); # ['a', 'b', 'c', 'd', 'e', 'g']
log.info(f'Output #3.6: {copy_my_list1}'); # ['a', 'b', 'c', 'd', 'e', 'f']

# 使用直接两个数组赋值（=）的形式进行浅拷贝
# 直接使用数组赋值，由于应用对象一致，会导致出现数据不独立，操作list后相互影响的问题
my_list2 = ['a', 'b', 'c', 'd', 'e'];
copy_my_list2 = my_list2;
log.info(f'Output #3.7: {my_list2}'); # ['a', 'b', 'c', 'd', 'e']
log.info(f'Output #3.8: {copy_my_list2}'); # ['a', 'b', 'c', 'd', 'e']
my_list2.append("f");
log.info(f'Output #3.9: {my_list2}'); # ['a', 'b', 'c', 'd', 'e', 'f']
log.info(f'Output #3.10: {copy_my_list2}'); # ['a', 'b', 'c', 'd', 'e', 'f']
copy_my_list2.append("g");
log.info(f'Output #3.11: {my_list2}'); # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
log.info(f'Output #3.12: {copy_my_list2}'); # ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# test
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
log.info('***************************test1********************************');
log.info(f'the first three item in the list are: {test_list[0 : 3]}');
log.info(f'the middle three in the list are: {test_list[3 : 6]}');
log.info(f'the last three in the list are: {test_list[-3 :]}');