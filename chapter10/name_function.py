def get_formatted_name(frist, last, middle=''):
    """
    生成规范格式的名字
    """
    if middle:
        full_name = f'{frist} {middle} {last}'
    else:
        full_name = f'{frist} {last}'
    return full_name.title()
