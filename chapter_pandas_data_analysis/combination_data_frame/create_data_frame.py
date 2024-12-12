import pandas as pd

def get_data_frame_user4():
    """按行创建一个DataFrame
    Returns:
        返回一个4行，拥有'name', 'age', 'country', 'score', 'continent'列
        并且拥有1001-1004作为索引的Dataframe
    """
    data = [['Mark', 55, 'USA', 4.5, 'America'],
            ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'China', 3.9, 'Asia'],
            ['Jenny', 12, 'Italy', 9.0, 'Europe']]
    return pd.DataFrame(data, 
                      columns=['name', 'age', 'country', 'score', 'continent'],
                      index=[1001, 1002, 1003, 1004])

def get_data_frame_user2():
    """
    Returns:
        拥有2行，拥有 age, country, name, score 列
        并且索引为1001和1011的DataFrame 
    """
    data = [[15, 'France', 'Becky', 4.1],
            [44, 'Canada', 'Leanne', 6.1]]
    return pd.DataFrame(data,
                        columns=['age', 'country', 'name', 'score'],
                        index=[1001, 1011])

def get_more_categories():
    """
    Returns:
        返回一个拥有两列数据，分别为 'quizzes', 'logins'
        索引为1001，2000的DataFrame
    """
    data = [[50, 100],
            [30, 70]]
    return pd.DataFrame(data,
                        columns=['quizzes', 'logins'],
                        index=[1001, 2000])