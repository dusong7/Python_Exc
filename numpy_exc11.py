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
