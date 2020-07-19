# 判断    
# if 条件1:
#     输出1
# elif 条件2:
#     输出2
# ......
# else：
#     输出3
"""
a = 1
b = 2 
if a>b:
    print("a比b大")
else:
    print("b比a大")

a = int(input("请输入成绩："))
if a > 100 or a < 0:
    print("成绩输入错误")
elif a >= 90:
    print("成绩优秀")
elif a >= 80:
    print("成绩良好")
elif a >= 70:
    print("成绩中等")
elif a >= 60:
    print("成绩及格")
else:
    print("成绩不及格")

a = input("请输入：")
if type(a) is int:
    print("整型")
elif type(a) is str:
    print("字符串")
else:
    print("其他")
"""
# 循环
# while循环
"""
a = 1
while a<10:
    print("哈哈")
    a+=1
"""
# 练习
# 10个学生的成绩录入到系统中
# 名字和成绩对应
# 大于60和小于60的成绩分开放
"""
studentlist = ["张三","李四","王五","小明","小红","小芳","嘟嘟","嘻嘻","哈哈","呵呵"]
a = 0
highchengji = {}
lowchengji = {}
while a < len(studentlist):
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji
    a = a+1
print("及格的成绩为：",highchengji)
print("不及格的成绩为：",lowchengji)
"""

# for循环 遍历效果
# range方法 生成一个整数列表
# range(a,b,c) 生成a到b-1的列表，左闭右开，步长c
"""
a = ["张三","李四","王五","小明","小红","小芳","嘟嘟","嘻嘻","哈哈","呵呵"]
for i in a:
    print(i)

for i in range(100):
    print(i)

for i in range(0,10,2):
    print(i)

studentlist = ["张三","李四","王五","小明","小红","小芳","嘟嘟","嘻嘻","哈哈","呵呵"]
highchengji = {}
lowchengji = {}
for i in studentlist:
    chengji = int(input("请输入"+i+"的成绩："))
    if chengji >= 60:
        highchengji[i] = chengji
    else:
        lowchengji[i] = chengji
print("及格的成绩为：",highchengji)
print("不及格的成绩为：",lowchengji)
"""
# 练习
# 打印九九乘法表
# end="a"的作用：以a结尾    print()换行
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")
    print()
"""
# 练习1：模拟红绿灯功能。红灯30次，绿灯35，黄灯3次
for a in range(1):
    for i in range(1,31):
        print("红灯还有",31-i,"秒结束")
    for j in range(1,36):
        print("绿灯还有",36-j,"秒结束")
    for k in range(1,4):
        print("黄灯还有",4-k,"秒结束")
# 练习2：注册功能
#     用户输入账号密码，要求账号长度5-8，密码长度6-12，并且账号必须小写字母开头，储存到字典中{username,password}
