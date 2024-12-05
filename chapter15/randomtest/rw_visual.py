import matplotlib.pyplot as plt # type: ignore

from random_walk import RandomWalk

def test_random_01():
    """绘制随机游走图"""
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s = 10)
    ax.set_aspect('equal')

    plt.show()

def test_random_02():
    """根据用户输入模拟多次随机游走"""
    while True:
        rw = RandomWalk()
        rw.fill_walk()

        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.scatter(rw.x_values, rw.y_values, s = 10)
        ax.set_aspect('equal')

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break

# test_random_02()

def test_random_03(numbers):
    """绘制随机游走图样式"""
    # 创建一个RandomWalk实例
    rw = RandomWalk(numbers)
    rw.fill_walk()

    plt.style.use('classic')
    # 自适应窗口
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_number, cmap = plt.cm.Blues, s = 10)
    ax.set_aspect('equal')

    # 突出起点和终点
    ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c ='red', edgecolors = 'none', s = 50)

    # 隐藏x轴和y轴
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    # 绘制x轴和y轴的网格
    ax.grid(True)

    plt.show()

test_random_03(50000)