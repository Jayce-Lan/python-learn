class RandomWalk:
    """随机游走数据的类"""

    def __init__(self, num_points=5000):
        """初始化一个随机游走的属性"""
        self.num_points = num_points

        # 所有点的 x 和 y 初始位置都为 0
        self.x_values = [0]
        self.y_values = [0]
    
    