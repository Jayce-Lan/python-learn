import matplotlib.pyplot as plt # type: ignore

"""
macOS通过pipx安装matplotlib后未能有效识别
只能通过以下语句，通过虚拟环境运行
pipx run --spec matplotlib -- python mpl_squares.py
"""

squares = [1, 4, 9, 16, 10]

fig, ax = plt.subplots()
# ax.plot(squares)

# 通过修改plot属性修改线条，此处为修改线条粗细
ax.plot(squares, linewidth=3)
# 设置表头与表头字体大小
ax.set_title("Square Numbers", fontsize=24)
# 设置x轴与y轴字体大小
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(axis='both', labelsize=14)

plt.show()