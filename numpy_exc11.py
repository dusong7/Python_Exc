from numpy import *
from math import *
import numpy as np

x = repeat(random.randn(5),2)
# print(x)

x.sort()
# print(x)

# unique(x)
ax = array([[1,6,2],[3,4,5],[1,5,7]])
print(ax)

print(ax.max(0))

a = random.randn(4)
print(a)
b = random.randn(4)
print(b)

print(maximum(a,b))

M,N = 5, 3

x = zeros((M,N), dtype= 'int32')
print(5*x)

##
x = arange(5)
print(x)
print(type(x))
print(x.view(matrix))

import mpl_toolkits.mplot3d as mp3d
import matplotlib.pyplot as plt

# x = np.linspace(0,6*np.pi,600)
# z = x.copy()
# y = np.sin(x)
# x=np.cos(x)
# fig = plt.figure()
# ax = mp3d.Axes3D(fig)
# ax.plot(x, y, zs=z)
# ax.view_init(15,45)
# # plt.show()
#
# list = [1,3,4,5]
# list1 = [13,33,43,52]
# plt.plot(list)
# plt.plot(list1)
# plt.show()
import time as tm
#
#
# for i in range(100):
#     print(tm.clock())
#     tm.sleep(1)

x = random.randn(4,3)
print(shape(x))
x.shape= 6,-1

print(x)

# from time import ctime
# from time import sleep
# import threading
#
# def music(func):
#     for i in range(2):
#         print("This is music %s_%s"%(func,ctime()))
#         sleep(1)
#
#
# def movie(func):
#     for i in range(2):
#         print("This is movie %s_%s" % (func, ctime()))
#         sleep(5)
#
# threads= []
#
# t1 = threading.Thread(target=music,args=("Love_",))
# threads.append(t1)
#
# t2 = threading.Thread(target=movie,args=("theSpeed_",))
# threads.append(t2)
#
# def run():
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#
#     print("All over_")
#
# if __name__ == "__main__":
#     run()

import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

def run1():
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print ("all over %s" %ctime())

if __name__ == '__main__':
    run1()
