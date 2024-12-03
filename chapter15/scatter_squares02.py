import matplotlib.pyplot as plt # type: ignore

################################
# 使用scatter绘制散点图
################################

# 手动传入数据
# x_axis = ['2020', '2021', '2022', '2023', '2024']
# y_axis = [1, 4, 9, 20, 15]

# 自动计算数据
x_axis = range(1, 1001)
y_axis = [x ** 3 for x in x_axis]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# 使用s设置绘图时使用的点的尺寸，并且传入x、y的坐标数组
# 使用color属性可以设置散点颜色，支持颜色和rgb的声明方式
# ax.scatter(x_axis, y_axis, s=6, color='red')
# ax.scatter(x_axis, y_axis, s=6, color=(0, 0.8, 0))

# 使用colormap颜色映射实现渐变，属性为cmap
ax.scatter(x_axis, y_axis, s=6, c=y_axis, cmap=plt.cm.Blues)

# 设置标签以及xy轴
ax.set_title("scatter test", fontsize=24)
ax.set_xlabel("x-axis", fontsize=14)
ax.set_ylabel("y-axis", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(axis='both', labelsize=14)

# 设置坐标轴范围，最外层的坐标只会获取到这个区间的坐标
# ax.axis([0, 900, 0 ,900_000])

# 展示图片
# plt.show()
# 保存图片
# 声明文件名，bbox_inches为是否保留空格
plt.savefig('scatter_plot.png', bbox_inches="tight")