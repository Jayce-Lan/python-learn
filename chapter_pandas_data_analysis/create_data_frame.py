import pandas as pd

def get_data_frame_5column():
    """按行创建一个DataFrame
    Returns:
        返回一个4行，拥有'Name', 'Age', 'Country', 'Score', 'Continent'列
        并且拥有1001-1004作为索引的Dataframe
    """
    data = [['Mark', 55, 'USA', 4.5, 'America'],
            ['John', 33, 'USA', 6.7, 'America'],
            ['Tim', 41, 'China', 3.9, 'Asia'],
            ['Jenny', 12, 'Italy', 9.0, 'Europe']]
    return pd.DataFrame(data, 
                      columns=['Name', 'Age', 'Country', 'Score', 'Continent'],
                      index=[1001, 1002, 1003, 1004])

def get_data_frame_only_number():
    """
    Returns:
    返回一个只有数字的，列名分别为city1-city3的Dataframe
    """
    data = {'city1': [100.1, 200],
            'city2': [300.3, 505],
            'city3': [1000.03, 1024]}
    return pd.DataFrame(data)

