import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# 字典类似于JSON，是以key-value形式存储信息
dict = {'name': 'Jayce', 'age': 29};
# 访问字典值
log.info(f'Output #1.1: {dict["name"]}');
log.info(f'Output #1.2: {dict["age"]}');

# 添加键值对
dict_2 = {};
dict_2['color'] = 'red';
dict_2['points'] = 5;
log.info(f'Output #2.1: {dict_2}');

# 修改字典值
dict_3 = {'color': 'green', 'points': 6};
log.info(f'Output #3.1: {dict_3}');

dict_3['color'] = 'blue';
log.info(f'Output #3.2: {dict_3}');

# 模拟外星人移动进行字典值修改
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'};
log.info(f'Output #3.3: {alien["x_position"]}');
alien['speed'] = 'fast';

# 外星人向X轴移动
if alien['speed'] =='slow':
    x_increment = 1;
elif alien['speed'] =='medium':
    x_increment = 2;
else:
    x_increment = 3;

alien['x_position'] = alien['x_position'] + x_increment;
log.info(f'Output #3.4: {alien["x_position"]}');
log.info(f'Output #3.5: {alien}');

# 使用 del 删除字典中的元素
test_del_value = {'color':'green', 'points': 5};
log.info(f'Output #4.1: {test_del_value}');

del test_del_value['points'];
log.info(f'Output #4.2: {test_del_value}');