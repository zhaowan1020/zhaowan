# 函数/方法的定义
# def 函数名(形参1,形参2):
#     函数体
"""
def check(username,password):
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password) >=6 and len(password) <=10: 
                return "账号，密码符合要求"
            else:
                return "密码长度必须是6-10"
        else:
            return "账号必须以小写字母开头"
    else:
        return "账号长度必须是5-8"
"""
# 函数/方法的调用
# 函数名(实参1，实参2)
"""
a = input("请输入账号：")
b = input("请输入密码：")
print(check(a,b))
"""
# 异常处理
# try:
#     <语句> #运行别的代码
# except： 
#     <语句> #如果在try部份引发了'name'异常
# except <名字>，<数据>:
#     <语句> #如果引发了'name'异常，获得附加的数据
# else:
#     <语句> #如果没有异常发生
"""
a = input("请输入姓名：")
b = input("请输入年龄：")
try:
    if int(b) >=18:
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄")
"""
#import 包名
# time时间
# random随机数
# 常用的第三方包：pymysql 操作数据库
#                selenium
#                appium
#                requests
# import pymysql
# pymysql.connect(host="127.0.0.1",user="zhaowan",password="zw991020",db="数据库名")
