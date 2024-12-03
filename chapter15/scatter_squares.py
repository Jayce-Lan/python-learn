import matplotlib.pyplot as plt # type: ignore

################################
# 使用scatter绘制散点图
################################

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# 使用s设置绘图时使用的点的尺寸
ax.scatter(2, 4, s=200)
# 设置标签以及xy轴
ax.set_title("scatter test", fontsize=24)
ax.set_xlabel("x-axis", fontsize=14)
ax.set_ylabel("y-axis", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(axis='both', labelsize=14)

plt.show()