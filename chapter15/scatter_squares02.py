import matplotlib.pyplot as plt # type: ignore

################################
# 使用scatter绘制散点图
################################

# 手动传入数据
# x_axis = ['2020', '2021', '2022', '2023', '2024']
# y_axis = [1, 4, 9, 20, 15]

# 自动计算数据
x_axis = range(1, 1001)
y_axis = [x ** 2 for x in x_axis]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# 使用s设置绘图时使用的点的尺寸，并且传入x、y的坐标数组
ax.scatter(x_axis, y_axis, s=6)

# 设置标签以及xy轴
ax.set_title("scatter test", fontsize=24)
ax.set_xlabel("x-axis", fontsize=14)
ax.set_ylabel("y-axis", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(axis='both', labelsize=14)

plt.show()