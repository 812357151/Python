import math
import random
import time
import calendar
# str="Hello World!"
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*2)
# print(str+" Test")   

# tuple=('runoob',786,2.23,'john',70.2)
# tinytuple=(123,'john')
# print (tuple)
# print(tuple[0])
# print(tuple[2:])
# print(tinytuple*2)
# print (tuple+tinytuple)
# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = input("Enter a number  :")
#    print ("You entered: ", num)
 
# print ("Good bye!")
# fruits = ['banana', 'apple',  'mango']
# print(len(fruits))
# print(dir(range(len(fruits))))
# for index in range(len(fruits)):
#    print ('当前水果 :', fruits[index])
 
# print ("Good bye!")

# print(abs(-1))


# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())

# # 生成同一个随机数
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())

# # 生成同一个随机数
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())

# list=[1,2,3]
# random.shuffle(list)
# print(list)

# print(random.uniform(4,10))
# print(math.cos(30))
# print(math.pi)
# print(math.e)
# print("the follow is test".center(30,'*'))
# print("123#123#".count('#'))
# print("isalnum()".center(20,"*"))
# print("123!".isalnum())
# print("abc".isalpha())
# print("*".join(("1","2","3")))
# print("123".partition("#"))
# list=[]
# list.append("1")
# list.append("2")
# print(list)
# del list[1]
# print(list)
# print(tuple(list))

# ticker=time.time()
# print("当前时间:",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# cal= calendar.month(2016,1)
# print(cal)

# def changeme( mylist ):
#    "修改传入的列表"
#    mylist.extend([1,2,3,4])
#    print ("函数内取值: ", mylist)
#    return
 
# # 调用changeme函数
# mylist = [10,20,30]
# changeme( mylist )
# print ("函数外取值: ", mylist)

# def printinfo(name,age):
#     print("name:",name)
#     print("age:",age)
#     return
# printinfo(age=50,name="miki")

# def printinfo(arg1,*argm):
#     print("first value:",arg1)
#     for argv in argm:
#         print(argv)
#     return
# print(1,2,3,4,5)

# sum=lambda avg1,agv2:avg1+agv2
# print(sum(1,2))

# import test2
# # test2.print_fun("22")
# Money = 2000
# def AddMoney():
#    # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
 
# print (Money)
# AddMoney()
# print (Money)

# print(dir(test2))
# try:
#     f= open("test2.py",'r')
#     print(f.read())
# finally:
#     f.close()

# import os,sys

# print(os.getcwd())
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")