# import Sum
#
# print "Hello"
#
# if __name__=="__main__":
#     Sum.getMul(3,5)
#
# # if __name__ == '__main__':
# #     import string
# #     fp = open('JCP099.py')
# #     a = fp.read()
# #     fp.close()
# #
# #     fp = open('JCP098.py')
# #     b = fp.read()
# #     fp.close()
# #
# #     fp = open('C.txt','w')
# #     l = list(a + b)
# #     l.sort()
# #     s = ''
# #     s = s.join(l)
# #     fp.write(s)
# #     fp.close()
#
# print 'What\'s your name'
# #
# # a = "python"
# # b = "on"
# #
# # print a-b

# import serial
# import time
# ser = serial.Serial('COM3', 9600, timeout=0)
#
# while True:
#     print ser.readline()
#
# import math
#
# inputNum = 0;
# targetNum =

# def func(x,y):
#     print "This is Function"
#     print x+y
#
# def func():
#     print "This is num"
#  ERROR
# func()
#
# x = 2
#
# def changeValue():
#     global x
#     x = 10
#     print x
#
# changeValue()
# print x
#
# 10
# 10
#
# def funcUntype(x, y ,*args, **kwargs):
#     print x
#     print y
#     print args
#     print kwargs
# #
# #     for i in args:
# #         print i
# #
# funcUntype(1,2,3,4)
#
# 1
# 2
# (3, 4)
# {}

#
# 1
# (2, 3, 4)
# 2
# 3
# # 4
# def foo(x, y=2, *targs, ** dargs):  //avoid content error
#       print x
#       print y
#       print targs
#       print dargs
#
# foo(1,2,"123","1233",d1="da", d2="d3")
#
# 1
# 2
# ('123', '1233')
# {'d2': 'd3', 'd1': 'da'}
#
# class Person:
#     def __init__(self, gender, tall="1", weight="1"):
#         self.gender = gender
#         self.tall = tall
#         self.weight = 1000
#
#     def Score(self,math="0", english="0"):
#         self.math = math
#         self.english = english
#
#     def ShowInfo(self):
#         print "Tall", self.tall
#
# class Programmer:
#     def __init__(self, name, gender, tall):
#         self.name = name
#         self.gender = gender
#         self.tall = tall
#
#     def pythoner(self):
#         pythoner_list = [self.name, self.tall, self.gender]
#         return pythoner_list
#
# writer = Person("M", 100,100)
# python = Programmer("Du", "M", "190")
#
# print writer.ShowInfo()
# print python.pythoner()
#
# Tall 100
# None
# ['Du', '190', 'M']

#
# Man = Person("M","122","100")
# Woman = Person("W")
#
# Man.Score(129,110)
# Woman.Score()
# print Woman.gender
# print Woman.tall
#
# print Man.weight
# print Man.gender
# print Man.tall
# print Man.english
#
# Man.ShowInfo()
# Woman.ShowInfo()
#
# W
# 1
# 1000
# M
# 122
# 110
# Tall 122
# English Score 110
# Tall 1
# English Score 0



# import math
#
# for i in range(1,12):
#     print "curVar%s mult is %d" %(math.pi*i,i)

# def out_foo():
#     a = 10
#     def inner_foo():
#         a = 20
#         print "innner_foo, a=", a
#
#     inner_foo()
#     print "out_foo, a = ", a
#
# a = 30
# out_foo()
# print "a=", a
#
# class MyClass:
#     def mufun(self, name):
#         print name
#
# a = MyClass()
# y = a.mufun
# y("name")
#
# """"Tihis is python lesson"""

# import tarimpo
#
# """print dir(tarimpo)""" ##comment this line
#
# tarimpo.myname("Dusong7")
# tar = tarimpo.tarimport("Java")
# tar.programmer()

# from tarimpo import *
# 
# Ja = tarimport("H")
# Ja.programmer()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print self.name
#     def __work(self,salary):
#         print "%s salary is %d"%(self.name,salary) ##private function
#     def showWorkInfo(self):
#         self.__work(500)
# 
# person = Person("Dusong")
# person.showWorkInfo()
# 
# Dusong
# Dusong salary is 500

# # coding=utf-8
# import sys
# __author__ = 'Administrator'
# x=0
# sum1=0
# #for x会自动+1
# for x in range(100):
#     sum1=x+sum1
# print sum1
# #while x需要自己加1
# x=0
# sum2=0
# while x in range(100):
#     sum2=x+sum2
#     x=x+1
# print sum2
# def addnum(a,b):
#     sum=0
#     while a<=b:
#      sum=a+sum
#      a=a+1
#     return sum
#
# print addnum(0,5)
#
# print addnum(int(sys.argv[1]),int(sys.argv[1]))
# import math
# print 123456789870987654321122343445567678890098876*1233455667789990099876543332387665443345566
# print 10.0/3
# print type(2435678.567)
# print round(1.23434,3)

# def sum_twonumber(a, b):
#     c = a + b
#     print c
#
# sum_twonumber(12,23)
# c=10240
# b=" Hello world_This_"
# print b
# print type(b)
# a = "This python"
# print a+b+`c`
# print "number is %d"%12
# a = "py"
# b = "thon"
# print "%s%s"%(a,b)
# a = "qwerty"
#
# print a.upper()
# a = "Hello, wo rld"
# print len(a)
#
# print a[-1]
# print a[11]
# print a[4]
# print a[6]
# print a[7]
# print a[12]
# print a[:]
# a = "Qiertegg, Python"
# b = "QEE"
# c = "qISWS"
# d = "Qu"
# e = 'Qiwsir,Github'
#
# f = b.title();
# print a.istitle();
# print b.istitle();
# print c.istitle();
# print d.istitle();
# print e.istitle();
# print f;
# print f.istitle();
## coding:utf-8
# print "please write your name"
# name = raw_input();
# name = name.title();
#
# print "Hello, %s%s"%(name,name)
# print not(4<3)
# a = raw_input();
#
# if(int(a)==4):
#     print "It is four"
# else:
#     print "It is not FOUR"
#
# a = "Hello"
# print bool(a)
#
# b = []
# print type(b)

# a = ["a", "cd", "wedede"]
# print a[1]
# a.append("yyy")
# print a
# a[3:] = ["rtyui"]
# print a.pop(1)
# print a
# print range(0,-9,-1)
# print range(0,9,2)
# pythoner = ["I", "am", "a", "pythoner", "I", "would", "like", "learn", "it"]
# print pythoner
# py_index = range(len(pythoner))
# print py_index

# num = [1,2,6,4,7,34,3,9,54]
# num.sort();
# print num
# num.sort(reverse=True)
# print num
#
# print sorted(num,reverse=True)
# help(list)
# line ="Hello. I am qiwsir. Welcome you"
# print line.split(".")
#
# name = "Du songchang"
# # print name.split(" ")
# ['Hello', ' I am qiwsir', ' Welcome you']
# ['Du', 'songchang']

# s = "I am Writing a line \nlearn Python\tlanguage on PyCharm"
# print s
# # I am Writing a line
# # Python	language on PyCharm
# print s.split()
# ['I', 'am', 'Writing', 'a', 'line', 'learn', 'Python', 'language', 'on', 'PyCharm']
# a = [1, 2]
# b = "This is a test"
# a.extend(b)
# print a
# [1, 2, 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't']
# la = [1, 2, 3, 1, 4, "a", "c", "d"]
# print la.count(1)
#
# print la[2:7]
#
# print 1 in la
#
# if "a" in la:
#     la.remove("a")
#     print la
# else:
#     print "a not in la"
#
# print range(1,100,3)
#
# welcome = "Welcone you"
# print welcome[:4]
#
# gitlist = ["dusong7", "github", "IO"]
# print gitlist[0]
# print gitlist[len(gitlist)-1]
# print gitlist[1:2]
# # Welc
# # dusong7
# # IO
# # ['github']
# gitlist.pop()
# print gitlist
# # ['dusong7', 'github']
# s = "Hello, I am dusong7\nThis is myTest\ton Windows"
# name = ["john", "Hoda", "Holla", "Bonjour"]
#
# print " ".join(name)
# print s.split()
# print "".join(s)
# Welc
# dusong7
# IO
# ['github']
# ['dusong7', 'github']
# john Hoda Holla Bonjour
# ['Hello,', 'I', 'am', 'dusong7', 'This', 'is', 'myTest', 'on', 'Wondows']
# Hello, I am dusong7
# This is myTest	on Wondows
#
# hello = "world"
# for i in hello:
#     print i +",",
# print len(hello)

# aliquot = []
# for n in range(1,100):
#     if n%3 == 0:
#         aliquot.append(n)
# print aliquot
#
# print range(1,100,3)
# import serial
# ser = serial.Serial()
# line = ser.readline()
# power2 = []
# for i in range(1,10):
#     power2.append(i*i)
#
# print power2
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print 2|1  # 10 OR 1 is equar 11
# print 3^5  # 11 XOR 101 is equar 110
# print 3**2 # 3^2 is equar 9
#
# aliquo = [n for n in range(0,10) if n%3]
# print aliquo
# [1, 2, 4, 5, 7, 8]
# seasons = ["Spr", "Summer", "Fal", "Winter"]
# print list(enumerate(seasons))
# [(0, 'Spr'), (1, 'Summer'), (2, 'Fal'), (3, 'Winter')]
# print dir(dict)
# import time
# print time.strftime();
# print time.strftime("%S%d%y");
# list_line = ["This", "Is", "a", "Test"]
#
# print len(list_line)
#
# for word in list_line:
#     print word

# Alphabet = {1:"A", 2:"B", 3:"C"}
# print Alphabet
# Alphabet[4]=["DDD"]
# print Alphabet
#
# for i in Alphabet:
#     print Alphabet[i]

# testList = [[1,2,3,4], [5,6], [7,8]]
#
# print testList[0][3]
#
# value is 4

# website = {1:"Google", 2:"Yahoo", 3:"Apple", 4:"Facebook"}
# print website.keys()
# print website.values()
# print website.items()
# [1, 2, 3, 4]
# ['Google', 'Yahoo', 'Apple', 'Facebook']

# t = 1, "23", (23,"Hello")
# t[0] = 12
# #value is Error  'tuple' object does not support item assignment
# # print t[0]
# n_set = set(['q','w','e'])
# f_set = set(['q','w'])
# print n_set > f_set
# print f_set.issubset(n_set)
# print n_set.issuperset(f_set)
# print n_set.union(f_set)
# print n_set.intersection(f_set)
# print n_set.difference(f_set)
#
# True
# True
# True
# set(['q', 'e', 'w'])
# set(['q', 'w'])
# set(['e'])

# l2 = [1,2,3]
# l2[0] = 99
# l1 = l2
#
# print l1
# print l2
# l1 = "123412341234FFFFF"
# l2 = "123412341234FFFFF"
#
# l3 = 12
# l4 = 12
#
# print l1 is l2
# print l3 is l4
# True
# True

# number = [1,2,3,4,5,6]
# number2 = []
#
# for i in  number:
#     i+=2
#     number2.append(i)
#
# print number2
# [3, 4, 5, 6, 7, 8]

# import time
# import random
#
# TargetNum = random.randint(0,100)
# InputNum = 0

# for i in range(0, 10):
#     InputNum = raw_input()
#     if(TargetNum == int(InputNum)):
#         print "WIN"
#         print InputNum
#     if(TargetNum > int(InputNum)):
#         print "LARGE THAN THIS"
#     if(TargetNum < int(InputNum)):
#         print "SMALL THAN THIS"

# while(int(InputNum) != TargetNum):
#     InputNum = raw_input()
#     if(TargetNum == int(InputNum)):
#         print "WIN"
#         print InputNum
#     if(TargetNum > int(InputNum)):
#         print "LARGE THAN THIS"
#     if(TargetNum < int(InputNum)):
#         print "SMALL THAN THIS"

# # coding=utf-8
# f = open("te.txt")
#
# for i in f:
#     f.write()
#     print i
#
# def show():
#     print "ShowFunc"
#
# Testa = 1
# Testb = 4
#
# print Testb,Testa
#
# Testb,Testa = [Testa, Testb]
#
# print Testb,Testa
# 4 1
# 1 4
# print help(eval)
# print eval("10+12")
# 22

# import math
# import datetime
# now = datetime.date.today()
# print now
# print "PI is %d"%math.pi
# print "PI is %10.3f"%math.pi
# PI is 3.14159265359
# print "PI is {PI.pi}".format(PI=math)
# PI is3.14159265359

# print "{0:X}, {0:o}, {0:b}".format(255, 255, 255)
# print "Please input any character"
# value = raw_input()
# result = value.isdigit()
# print result
# print value

# x = [1, 2, 3]
# y = [4, 5, 6]
#
# for a,b in zip(x,y):
#     print a,b

# testList = [1,2,3,4,5,6,7,8]

# for i in testList:
#     print i
# listInte = iter(testList)
#
# while True:
#     print listInte.next()

# def add(val):
#     val+=3
#     print val
#
# add(13)

# nums = [1,2,3,4,5,6,7,8,9]
# lam = lambda x:x+3
#
# n2 = []
#
# for i in nums:
#     n2.append(lam(i))
#
# print n2
#
# num = [4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# print map(lambda x:x**2, num)

# print num
#
# [16, 25, 36, 49, 64, 81, 100, 121, 144]
# [4, 5, 6, 7, 8, 9, 10, 11, 12]

# print reduce(lambda x,y:x*y, num)
# 72
#
# x = 3
#
# def fun():
#     global x
#     x = 9
#     print "This x is "
#
# fun()

# class A(object):
#     def method1(self):
#         print "Method A"
#     def method2(self):
#         print "Method A1"
#
# class B(A):
#     def method3(self):
#         print "method B"
#
# class C(A):
#     def method2(self):
#         print "methodC2"
#
#     def method3(self):
#         print "MethodC3"
#
# class D(B,C):
#     def method4(self):
#         print "C.method4"
#
#
# d = D()
# d.method1()
# d.method2()
# d.method3()
# # d.method4()
# Method A
# methodC2
# method B
# C.method4
#
# import this
# print globals()

