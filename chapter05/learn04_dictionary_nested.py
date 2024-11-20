import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# 字典的嵌套
alien_0 = {'color': 'green', 'points': 5};
alien_1 = {'color': 'blue', 'points': 3};
alien_2 = {'color': 'red', 'points': 1};

# 字典列表
aliens = [alien_0, alien_1, alien_2];
for alien in aliens:
    log.info(f'Output #1: {alien}');

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 描述顾客所点披萨
log.info(f'Output #2.1: You ordered a {pizza.get('crust')} - crust pizza');
log.info(f'Output #2.1: You ordered a {pizza.get('test')}'); # 默认返回None
for topping in pizza.get('toppings'):
    log.info(f'Output #2.2: {topping}');

# 字典中存储列表一般用于处理一对多的关系
favorite_languages = {
    'Alice': ['Python', 'Java', 'C'],
    'Bob': ['C'],
    'Charlie': ['Java', 'JavaScript', 'Python'],
}
for coder, languages in favorite_languages.items():
    msg = f'Output #3.1: {coder} like language'
    if len(languages) > 1:
        msg += ' are:'
    else:
        msg += ' is:'
    log.info(msg);
    for language in languages:
        log.info(f'Output #3.2: {language}');

# 字典中嵌套字典
users = {
    'alen': {
        'name': 'Alen',
        'age': 20,
        'hobbies': ['reading', 'coding'],
    },
    'bob': {
        'name': 'Bob',
        'age': 25,
        'hobbies': ['painting', 'coding'],
    },
}

for user, msg in users.items(): 
    log.info(f'Output # 4.1: {user}: ');
    for key, value in msg.items():
        log.info(f'Output # 4.2: {key}: {value}');
