import logging
import logging.config
import os

# 获取当前文件名（不包括扩展名）
current_filename = os.path.splitext(os.path.basename(__file__))[0];
# 加载日志配置文件
logging.config.fileConfig('logging.conf');
# 获取logger对象，名称为当前文件名
log = logging.getLogger(current_filename);

favorite_languages = {
    'Tony': 'C',
    'Jony': 'Python',
    'James': 'Java',
    'Tom': 'Python'
}

coders = ['Tony', 'Jony', 'James', 'Tom'];
for coder in coders:
    if coder in favorite_languages:
        log.info(f'Output #1.1: {coder} likes {favorite_languages[coder]}');

# 使用 get(key, value2)  获取字典中的值
# key为对应的key，因为使用dict[key]时，key若不存在则会报错
# 而使用get可以在key不存在时返回value2
log.info(f'Output #2.1: {favorite_languages.get("Tony", "Unknown")}');
log.info(f'Output #2.2: {favorite_languages.get("Lisa", "Unknown")}');
log.info(f'Output #2.3: {favorite_languages['Tony']}');
log.info(f'Output #2.4: {favorite_languages['Lisa']}'); # 报错