import plotly.express as px # type: ignore 使用plotly.express绘制直方图
# 需要依赖：plotly/pandas/matplotlib
# macOS中，当需要引入多个依赖时，启用虚拟环境，并且安装依赖

import logging
import logging.config
import os

from die import Die

current_filename = os.path.splitext(os.path.basename(__file__))[0];
logging.config.fileConfig('logging.conf');
log = logging.getLogger(current_filename);

def test_die(die, num):
    """
    @param die: 色子对象
    @param num: 色子投掷次数
    @return: 骰子投掷结果
    """

    results = []
    # 投掷num次的结果，存储在数组中
    for roll_num in range(num):
        results.append(die.roll_die())

    return results

# 创建一个6面骰子
die_6 = Die(6)
# print(test_die(die_6, 100))

def count_die_visual(die, results = []):
    """
    @param die: 色子实体
    @param results: 色子的投掷结果
    @return: 进行结果分析，分析每个面出现次数
    注意：results参数是可选的，如果不提供，那么会创建一个空列表
    """
    frequencies = []
    poss_results = range(1, die.sides + 1)
    for value in poss_results:
        frequencies.append(results.count(value))
    return frequencies

roll_num = 1000
print(count_die_visual(die_6, test_die(die_6, roll_num)))

def show_die(die, frequencies = []):
    """
    @param die: 色子实体
    @param frequencies: 色子每一面的出现次数
    注意：frequencies参数是可选的，如果不提供，那么会创建一个空列表
    @return:
    展示色子执行结果
    """
    poss_results = range(1, die.sides + 1)

    # 定制绘图
    labels = {
        'x': '色子面数',
        'y': '每一面出现的次数'
    }
    title = f'{die_6.sides}面色子抛{roll_num}次的结果分布情况图'
    fig = px.bar(x = poss_results, y = frequencies,
                 title = title, labels = labels)
    fig.show() 

# show_die(die_6, count_die_visual(die_6, test_die(die_6, roll_num)))

def count__more_die_visual(roll_count, die_list = []):
    """
    @param roll_count: 色子投掷次数
    @param die_list: 多个色子组成的list
    @return:
    返回多个色子执行结果
    """
    # 存储色子投掷结果
    results = []
    for index in range(roll_count):
        die_sum = 0
        for die in die_list:
            die_sum += die.roll_die()
        results.append(die_sum)
    
    # 统计色子每个和的出现次数
    frequencies = []
    # 色子个数
    die_count = len(die_list)
    # 所有色子点数相加的最大和
    max_result = get_die_list_max_sum(die_list)
    # 进行结果遍历，获取到每个结果的分布情况
    for value in range(die_count, max_result + 1):
        frequencies.append(results.count(value))
    return frequencies

def show_more_die(die_list = [], frequencies = []):
    """
    @param die_list: 多个色子的列表
    @param frequencies: 多个色子每一面相加只和的出现次数
    @return: 展示统计结果
    """
    # 色子个数(因为色子最小数为1，因此色子个数就是所有色子最小和)
    die_min_sum = len(die_list)
    # 所有色子点数相加的最大和
    die_max_sum = get_die_list_max_sum(die_list)
    poss_results = range(die_min_sum, die_max_sum + 1)
    labels = {
        'x': '色子之和',
        'y': '每个数字出现的次数'
    }
    title = f'{len(die_list)}个色子抛{roll_num}次的面数之和结果分布情况图'
    fig = px.bar(x = poss_results, y = frequencies,
                 title = title, labels = labels)
    # 柱状图如果过多，会造成x轴标签间隔展示，此时可以定制图形
    # 间隔为1，并且每个柱状图都有标签
    fig.update_layout(xaxis_dtick = 1)

    fig.show() 

def get_die_list_max_sum(die_list):
    """
    @param die_list: 多个色子的列表
    @return: 所有色子点数相加的最大和
    """
    max_result = 0
    for die in die_list:
        max_result += die.sides
    return max_result

# 创建2个6面色子
die1 = Die()
die2 = Die(10)
die3 = Die()
die_list = [die1, die2, die3]
frequencies = count__more_die_visual(roll_num, die_list)
log.info(f'结果集： {frequencies}')
show_more_die(die_list, frequencies)
