import plotly.express as px # type: ignore 使用plotly.express绘制直方图
# 需要依赖：plotly/pandas/matplotlib
# macOS中，当需要引入多个依赖时，启用虚拟环境，并且安装依赖
# 安装完毕后使用 python xxx.py来执行即可

from die import Die

def test_die(die, num):
    """
    测试骰子投掷
    @param die 色子对象
    @param num 色子投掷次数
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
    进行结果分析，分析每个面的次数
    @param die 色子实体
    @param results 色子的投掷结果
    @return: 色子每一面的出现次数
    注意：results参数是可选的，如果不提供，那么会创建一个空列表
    """
    freqyencies = []
    poss_results = range(1, die.sides + 1)
    for value in poss_results:
        freqyencies.append(results.count(value))
    return freqyencies

print(count_die_visual(die_6, test_die(die_6, 1000)))


poss_results = range(1, die_6.sides + 1)
frequencies = count_die_visual(die_6, test_die(die_6, 1000))
fig = px.bar(x = poss_results, y = frequencies)
fig.show() 
