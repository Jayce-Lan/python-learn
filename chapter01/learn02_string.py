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

# 也可以事先拼接字符
message = f"{first_name} {last_name}";
print(message);

# 空白符号（制表符）
print("Output #1: \tpython");
# 换行符号 此处打印先换行后前方带制表符的情况
print("Output #2: \n\tpython\n\tC\n\tJava");

# 删除空白
favorite_luanguge = " Python ";
print(f"Output #3: '{favorite_luanguge}'");

# lstrip() 删除左侧空白；rstrip()删除右侧空白；strip()删除左右两侧的空白
print(f"Output #4.1: '{favorite_luanguge.rstrip()}'");
print(f"Output #4.2: '{favorite_luanguge.lstrip()}'");
print(f"Output #4.3: '{favorite_luanguge.strip()}'");

# 结果不做存储，需要用变量承接
print(f"Output #5: '{favorite_luanguge}'");
# 承接结果
favorite_luanguge = favorite_luanguge.rstrip();
favorite_luanguge = favorite_luanguge.lstrip();
print(f"Output #6: '{favorite_luanguge}'");

# 删除前缀
# 使用 removeprefix() 删除前缀，如果前缀匹配失败，则不做任何操作
# 但是它不改变原始字符串的值，需要用变量承接才能做结果存储
nostarch_url = "https://nostarch.com/";
print(f"Output #7: '{nostarch_url.removeprefix("https://")}'");
print(f"Output #8: '{nostarch_url}'");
nostarch_url = nostarch_url.removeprefix("https://");
print(f"Output #9: '{nostarch_url}'");
# 删除后缀
# 使用 removesuffix() 删除后缀，用法与 removeprefix 一致
file_name = "learn02_string.txt";
print(f"Output #10: '{file_name.removesuffix('.txt')}'");
print(f"Output #11: '{file_name}'");

#test
said_msg = 'Hello, he said :"do yourself!"';
print(f"#Output #12: {said_msg}");