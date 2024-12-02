import matplotlib.pyplot as plt # type: ignore

# 定义x轴
x_values = [1, 2, 3, 4, 5]
# 定义y轴
y_values = [1, 4, 9, 20, 15]

fig, ax = plt.subplots()
# 加载自定义的x轴和y轴
ax.plot(x_values, y_values, linewidth=3)

plt.show()