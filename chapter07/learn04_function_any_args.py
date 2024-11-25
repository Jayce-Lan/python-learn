import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# ----------------------------------------------------------------
# 传递任意数量的实参
# 使用“*参数的”形式创建一个元组，该元组包含函数收到的所有值
# ----------------------------------------------------------------
def make_pizza(*toppings):
    """
    打印顾客点的传入的任意数量配料的参数
    """
    log.info(f'Output #1: Making a pizza with the following toppings:')
    for topping in toppings:
        log.info(f'Output #1: Adding {topping} to the pizza')

make_pizza('mushrooms', 'extra cheese', 'pepperoni')
make_pizza('prpperoni')

# ----------------------------------------------------------------
# 结合使用位置实参和任意数量的实参
# ----------------------------------------------------------------
def make_pizza_with_size(size, *toppings):
    """
    在这里，第一个参数会传入size，而后面的参数才是配料
    """
    log.info(f'Output #2: Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        log.info(f'Output #2: Adding {topping} to the pizza')

make_pizza_with_size(12, 'mushrooms', 'extra cheese', 'pepperoni')
make_pizza_with_size(16, 'prpperoni')

# ----------------------------------------------------------------
# 使用任意数量的关键字实参
# 当我们需要任意数量的实参，但是却不知道函数会传入什么信息时
# 可以将函数编写成能接收任意键值对的字典，使用“**参数”来作为参数
# 此时只有填入才添加键值对，否则不添加相应键值对
# ----------------------------------------------------------------
def build_profile(first_name, last_name, **user_info):
    """
    创建一个字典，里面包含已知的有关用户的信息
    """
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile1 = build_profile('Elon', 'Musk')
log.info(f'Output #3: {user_profile1}')
user_profile2 = build_profile('Jane', 'Smith', 
                              location='New York', 
                              field='Engineering')
log.info(f'Output #3: {user_profile2}')

