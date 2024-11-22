import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

# tips：与Java不同，方法注释必须写在方法里
# 使用“"""”作为开头结尾，这样在ide中调用方法时才能展示方法注释
def greet_users(users):
    """
    传入列表，向列表里的每个人问好
    """
    for user in users:
        log.info(f'Output #1: Hello, {user}!')

users = ['Musk', 'Bill', 'Coke', 'John']
greet_users(users)

# ----------------------------------------------------------------
# 使用函数处理列表
# ----------------------------------------------------------------
def print_models(unprint_models, complete_models):
    """
    @param unprint_models 未打印的材料
    @param complete_models 已打印的材料
    模拟材料打印，将已经打印的材料放入到complete_models中
    """
    while unprint_models:
        print_model = unprint_models.pop(0)
        log.info(f'Output #2.1: Printing {print_model}...')
        complete_models.append(print_model)

def show_complete_models(complete_models):
    """
    展示已打印材料
    """
    log.info(f'Output #2.1: the following have been printed:')
    for item in complete_models:
        log.info(f'Output #2.2: {item}')

unprint_models = ['Metal', 'Plastic', 'Wood', 'Glass']
complete_models = []
print_models(unprint_models, complete_models)
show_complete_models(complete_models)
log.info(f'Output #2.1: {unprint_models}')

# ----------------------------------------------------------------
# 禁止函数修改列表
# 上述的print_models方法会改变入参的两个列表
# 但是有时候我们并不希望传入的某个列表被处理，此时就可以进行深拷贝操作
# ----------------------------------------------------------------
unprint_models = ['Metal', 'Plastic', 'Wood', 'Glass']
complete_models = []
# 使用切片进行列表深拷贝，防止原列表被处理
# 但是在日常处理，尤其处理大型列表时不建议这样做，创建列表副本会造成不必要的开销
print_models(unprint_models[:], complete_models)
show_complete_models(complete_models)
log.info(f'Output #2.1: {unprint_models}')
