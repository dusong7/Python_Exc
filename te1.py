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
