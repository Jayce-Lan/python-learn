name = "ada love lace";
# Ada Love Lace 首字母大写
print(name.title());
# 完全大写
print(name.upper());
# 完全小写
print(name.lower());

# 在字符串中使用变量
first_name = "ada";
last_name = "aba";
# 在字符串中加入变量的值可以使用 f"…{}…"的形式进行插入，在{}中放入变量"
# f是 format()函数的缩写
print(f"Hello, {first_name} {last_name}!");
# 等同于
print("Hello, {0} {1}!".format(first_name, last_name));
