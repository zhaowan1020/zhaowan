# print("hello world!")
# a = int(input())
# b = int(input())
# print(a+b)
# print(type(223330))
# print(type(True))

# a = input("输入第一段内容")
# b = input("输入第二段内容")
# print("两段内容的长度为",len(a)+len(b))

#元组(),下标[]从0开始
#倒着数-1，-2
# a = (1,2,3,4,"哈哈哈","哈哈哈","哈哈哈",True,False)
# print(a)
# print(a[4])

# 切片
# print(a[2:5])   #左闭右开
# print(a[2:])    #右不写到最后
# print(a[:3])    #左不写从头开始
# index查找下标
# # count统计某个值的数量
# print(a.count("哈哈哈"))
# print(a.index(3))

# 二维元组
# b = (a,"哈哈哈","嘻嘻")
# print(b)
# print(b[2])
# print(b[0][2])

# 数组
# a = [1,2,3,4,"哈哈哈","嘻嘻",True,False]
# print(a)
# index，count操作和元组一样
# 区别:元组写好后不可以修改，数组可以修改

# 添加内容,在最后
# a.append("哈哈哈")  
# print(a)

# 在指定的位置插入数据insert(下标，内容)
# a.insert(4,"呵呵呵")
# print(a)    

# 剪切数据
# b = a.pop(5)
# print(a)
# print(b)

# 清空数组
# a.clear()

# 数组中插入数组(合并数组)
# c = [123456,1515]
# a.extend(c)
# print(a)

# 删除数组中的值
# a.remove("嘻嘻")
# print(a)

"""
python的语法
所有的方法都是()结尾
元组、数组、字典的取值，都是用[]
元组、数组、字典的定义分别是()、[]、{}
"""

"""
字典
1、字典中的值没有顺序
2、字典的结构必须是键值对的结构 key:value
3、字典的取值是通过可以去取value
"""
# a = {"name":"张三","age":"18","sex":"男"}
# print(a)

# 取值
# print(a["name"])

# 新增
# a["high"] = 180
# print(a)

# 修改
# a["name"] = "李四"
# print(a)

# get方法 取值
# b = a.get("name")
# print(b)

# pop方法 剪切
# b = a.pop("name")
# print(b)

# update方法 新增或修改
# a.update(name="王五")
# print(a)

# 数组和字典的删除
# del a["name"]
# print(a)

# 获取用户输入个人信息并且存储到字典中。
# 个人信息包括name,age,sex
# a = input("请输入姓名：")
# b = input("请输入年龄：")
# c = input("请输入性别：")
# d = {"name":a,"age":b,"sex":c}
# print("个人信息:",d)

