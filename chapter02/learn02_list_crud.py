import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki'];
log.info(f"Output #1: {motorcycles}"); # ['honda', 'yamaha', 'suzuki']
# 使用数组下标修改
motorcycles[0] = 'ducati';
log.info(f"Output #2: {motorcycles}"); # ['ducati', 'yamaha', 'suzuki']


# 添加元素
# 使用 append(value) 在数组末尾添加元素
motorcycles.append('bmw');
log.info(f"Output #3: {motorcycles}"); # ['ducati', 'yamaha', 'suzuki', 'bmw']
# 使用 insert(index, value) 在列表中插入元素，index为插入的下标

motorcycles.insert(1, 'kawasaki');
log.info(f"Output #4: {motorcycles}"); # ['ducati', 'kawasaki', 'yamaha', 'suzuki', 'bmw']
# 当index大于数组长度时，默认插入最后一位
motorcycles.insert(7, 'kawasaki');
log.info(f"Output #4.1: {motorcycles}"); # ['ducati', 'kawasaki', 'yamaha', 'suzuki', 'bmw']
# 当index为负数时，如果负数绝对值大于数组长度，那么插入数组首位；如果小于数组长度且小于0，则插入从数组尾部开始计算的绝对值index位
motorcycles.insert(-1, 'RR');
log.info(f"Output #4.2: {motorcycles}"); # ['ducati', 'kawasaki', 'yamaha', 'suzuki', 'bmw', 'RR', 'kawasaki']


# 删除元素

# 当删除后不需要被删除元素信息时，用del，但删除后需要被删除元素信息使用pop
# 使用 del 删除指定下标元素
del motorcycles[1];
# del motorcycles[6]; # index超过数组最大下标时，数组下标越界
log.info(f"Output #5: {motorcycles}"); # ['ducati', 'yamaha', 'suzuki', 'bmw', 'RR', 'kawasaki']

# 使用 pop() 删除最后一位元素
motorcycles = ['honda', 'suszuki', 'yamaha'];
popped_motorcycle = motorcycles.pop(); # 承接被删除的元素
log.info(f"Output #6.1: {motorcycles}"); # ['honda', 'suszuki']
log.info(f"Output #6.2: {popped_motorcycle}"); # yamaha
# 也可以使用 pop(index) 删除指定下标元素
motorcycles = ['honda', 'suszuki', 'yamaha'];
popped_motorcycle = motorcycles.pop(0); # 该方法也会存在数组下标越界的问题
log.info(f"Output #6.3: {motorcycles}"); # ['suszuki', 'yamaha']
log.info(f"Output #6.4: {popped_motorcycle}"); # honda

# 使用 remove(value) 删除数组指定元素(如果有多个value，只删除第一个)
motorcycles = ['honda', 'yamaha', 'suzuki', 'yamaha'];
motorcycles.remove('yamaha');
log.info(f"Output #7: {motorcycles}"); # ['honda', 'suzuki', 'yamaha']
