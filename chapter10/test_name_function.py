from name_function import get_formatted_name

def test_get_formatted_name():
    """
    能处理像 Janis Joplin这样的姓名吗
    """
    formatted_name = get_formatted_name('janis', 'joplin')
    # 断言，就是声称满足特定的条件；此处声称满足Janis Joplin
    assert formatted_name == 'Janis Joplin'

def test_get_formatted_name_middle():
    """
    能处理像 Janis Joplin这样的姓名吗
    """
    formatted_name = get_formatted_name('janis', 'joplin', 'm')
    # 断言，就是声称满足特定的条件；此处声称满足Janis Joplin
    assert formatted_name == 'Janis M Joplin'