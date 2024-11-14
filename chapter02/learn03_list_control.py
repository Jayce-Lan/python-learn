import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

# list排序
# 使用sort对list永久排序，顺序无法还原
cars = ['bens', 'bmw', 'toyota', 'audi', 'honda'];
# 默认进行升序排序
cars.sort();
log.info(f"Output #1.1: {cars}"); # ['audi', 'bens', 'bmw', 'honda', 'toyota']
# 传入 reverse = True 进行反向排序
cars = ['bens', 'bmw', 'toyota', 'audi', 'honda'];
cars.sort(reverse=True);
log.info(f"Output #1.2: {cars}"); # ['toyota', 'honda', 'bmw', 'bens', 'audi']

# 使用 sorted 对list进行临时排序，结果需要用变量承接，否则不做保存
cars = ['bens', 'bmw', 'toyota', 'audi', 'honda'];
log.info(f'Output #2.1: {sorted(cars)}'); # ['audi', 'bens', 'bmw', 'honda', 'toyota']
# 反向排序
log.info(f'Output #2.2: {sorted(cars, reverse=True)}'); # [['toyota', 'honda', 'bmw', 'bens', 'audi']
log.info(f'Output #2.3: {cars}'); # ['bens', 'bmw', 'toyota', 'audi', 'honda']

# 使用reverse方向打印列表，需要恢复list时，再次调用该方法即可
cars = ['bens', 'bmw', 'toyota', 'audi', 'honda'];
cars.reverse();
log.info(f'Output #3.1: {cars}');
cars.reverse();
log.info(f'Output #3.2: {cars}');

# 使用len确定数组长度
cars = ['bens', 'bmw', 'toyota', 'audi', 'honda'];
log.info(f'Output #4: {len(cars)}'); # 5

# index
cars = ['bens', 'bmw', 'audi'];
log.info(f'Output #5.1: {cars.index("bmw")}') # 1
# -1返回最后一个元素，除非list为空
log.info(f'Output #5.2: {cars[-1]}') # audi
# cars = []; # 导致下标越界
log.info(f'Output #5.3: {cars[-1]}') # audi

