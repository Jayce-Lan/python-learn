# 整数integer
# 整数可以进行 加+ 减- 乘* 除/ 操作；也支持像数学一样的计算顺序
print(f"Output #1: {2 + 3}");
print(f"Output #2: {2 - 3}");
print(f"Output #3: {-2 * 3}");
print(f"Output #4: {2 / 3}");
# 乘方
print(f"Output #5: {2 ** 3}");

print(f"Output #6: {2 - 3 * 4}");
print(f"Output #7: {(2 - 3) * 4}");

# 浮点数(float)
print(f"Output #8: {0.1 + 0.1}");
print(f"Output #9: {0.2 + 0.2}");
print(f"Output #10: {0.2 - 0.2}");
print(f"Output #11: {0.2 - 0.1}");
# 也会存在部分精度问题
print(f"Output #12: {0.1 + 0.2}"); # 0.30000000000000004
print(f"Output #13: {3 * 0.1}"); # 0.30000000000000004

# 整数和浮点数
print(f"Output #14: {2 + 3.0}");
print(f"Output #15: {2 - 3.0}");
print(f"Output #16: {2 * 3.0}");
print(f"Output #17: {4 / 2}"); # 只要是除法，即使整除结果也是浮点数

# 数中的下划线
# 当需要书写大数字时，为了易读，可以使用“_”分位，实际操作时分位符会被忽略
num1 = 1_000_000;
print(f"Output #18: {num1}"); # 1000000

# 同时给多个变量赋值
x, y = 1, 2;
print(f"Output #19: {x}, {y}");

# 常量
# 常量是整个生命周期都不做变动的变量，python中没有常量，但是一般使用纯大写来将某个变量标识为常量
MAX_VALUE = 100;
print(f"Output #20: {MAX_VALUE}");