import matplotlib.pyplot as plt # type: ignore

# 定义x轴
x_values = [1, 2, 3, 4, 5]
# 定义y轴
y_values = [1, 4, 9, 20, 15]

# ----------------------------------------------------------------
# 设置图表样式
# 图表的样式需要在图表被加载前进行声明
# ----------------------------------------------------------------
# 展示图表的样式
print(plt.style.available)
# 设置样式
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
# 加载自定义的x轴和y轴
ax.plot(x_values, y_values, linewidth=3)

# 设置表头与表头字体大小
ax.set_title("Square Numbers", fontsize=24)
# 设置x轴与y轴字体大小
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

plt.show()