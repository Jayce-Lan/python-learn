import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

user = {
    'user_name': 'Athena',
    'first_name': 'Tom',
    'last_name': 'Hattan'
}

# 使用for-in遍历字典，要调用字典的 “items()”方法
# items()会将字典变成一个类似二维数组的键值对列表，例如下面的打印结果为：
# dict_items([('user_name', 'Athena'), ('first_name', 'Tom'), ('last_name', 'Hattan')])
log.info(f'Output #1.1: {user.items()}');

# 使用for-in遍历字典的键值对
for key, value in user.items():
    log.info(f'Output #1.2: {key}: {value}');

# 使用for-in便利字典的所有键
# 方法一：使用keys()
# keys()可以将字典的键取出，并生成一个数组
# ['user_name', 'first_name', 'last_name']
log.info(f'Output #2.1: {list(user.keys())}');

for key in user.keys():
    log.info(f'Output #2.2: {key}');

# 在遍历字典时，默认遍历所有键，因此也可以改为
for key in user:
    log.info(f'Output #2.3: {key}');

favorite_languages = {
    'Tony': 'C',
    'Jony': 'Python',
    'James': 'Java',
    'Tom': 'Python'
}

friends = ['James', 'Tom'];

for name in favorite_languages:
    log.info(f'Output #2.4: Hi, {name}!');
    if name in friends:
        log.info(f'Output #2.4: {name} likes {favorite_languages[name]}');

# 使用sorted按照顺序遍历键
for name in sorted(favorite_languages):
    log.info(f'Output #2.5: Hi, {name}!');

# 遍历所有的值
log.info(f'Output #2.6: {favorite_languages.values()}');
for language in favorite_languages.values():
    log.info(f'Output #2.6: {language}');

# 上述方法中，值会有重复的情况发生，使用set承接可以过滤重复
log.info(f'Output #2.7: {set(favorite_languages.values())}');
for language in set(favorite_languages.values()):
    log.info(f'Output #2.7: {language}');
