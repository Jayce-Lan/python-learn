# Python学习内容

### 主要项目文件夹目录与对应说明

##### chapter_pandas_data_analysis

`pandas` 实现数据分析（针对DataFrame和Series）

> combination_data_frame

`DataFrame` 组合相关

- `concat` 连接多个DataFrame
- `join` 通过索引连接两个DataFrame
- `merge` 通过列连接两个DataFrame
- `pivot_table_and_melt` 通过`pivot_table`方法透视图表；使用`melt`方法反透视图表

> control_data

操作DataFrame

- `change_data` 修改DataFrame数据

- `none` 空值

- `duplicate` 重复数据

- `arithmetic` 算数运算

- `str` 字符串

- `applymap` 应用函数

> read_data

读取DataFrame

- `dataframe_row` 通过`pandas` 将Excel内容读取为DataFrame；按行数据创建DataFrame

- `dataframe_column` 通过列数据创建DataFrame

- `select_data` 使用`loc`方法和`iloc`（索引）读取DataFrame

- `select_data_by_boolean` 通过布尔值选择数据

- `select_data_by_multi_index` 通过MultiIndex（多级索引）将数据分组（类似group by操作）



##### chapter01

hello world，简单的语法学习

##### chapter02

list的增删改查与操作

##### chapter03

- `for` for循环的一些属性与样例

- `number_list` 使用for循环的属性创建list，并操作list；数值列表的简单计算（原生`sum`、`min`、`max` 函数在list中的应用）

- `list_handle` list的切片、深浅拷贝以及操作

- `tuple` 元组（无法修改的list）

##### chapter04

if判断语句的使用，以及for循环与if的混合使用

##### chapter05

字典值，类似于JSON格式的数据类型

- `dictionary` 字典值的创建与读取

- `dictionary_read` 字典值的`get[key]` 方法读取字典值

- `dictionary_iteration` 字典值的遍历

- `dictionary_nested` 字典值的嵌套（列嵌套字典、字典嵌套列、字典嵌套字典）

##### chapter06

输入输出与while循环

- `input` 简单的控制台输入

- `input_int` 控制台输入文本数据转为纯数字

- `while`/`while_flag`/`while_brea` / `while_continue` while循环的应用、退出与跳过

- `while_list` 使用while属性遍历list，移除list元素

- `while_dict` 使用while循环+input录入字典值

##### chapter07

- 方法的声明

- 方法形参的声明（多形参、是否为空、是否为默认值）

- 导入自定义包/导入外部包（`from`与`import` 关键字）

##### chapter08

class的声明与使用

##### chapter09

- `read_file` 读取txt文件

- `write_file` 写入txt文件

- `error` 异常处理（异常捕获、异常静默）

- `send_data` 将字典数据存储进本地json文件中

- `reconstitution` 方法重构，将learn04的方法进行重构

##### chapter10

使用`pytest`测试方法

- `name_function`/`names`/`survey` 被测试的类

- `test_name_function` 测试name_function的类，使用`assert`断言进行测试

- `test_surevery_fixtrue` 使用`@pytest.fixture`构造测试对象，让整个py文件都可以使用这一个对象

##### chapter15

使用`matplotlib`进行绘图
