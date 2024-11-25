# 导入指定模块，并使用mp给函数指定别名
from module.pizza import make_pizza as mp

# 通过别名调用方法
mp(12, 'mushrooms', 'extra cheese', 'pepperoni')