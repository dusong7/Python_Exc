import psutil
import time
import matplotlib.pyplot as plt
#
# def getProcessInfo(p):
#     try:
#         cpu = int(p.get_cpu_percent(interval=0))
#     except psutil.error.NoSuchProcess:
#         cpu = 0
#     return cpu
#
# p = psutil.Process(4956)
# print(p)
# list = []
# time = 0
# while time<100:
#     # print(p.cpu_percent(interval=1))
#     list.append(p.cpu_percent(interval=1))
#     time+=1

# import random
# list=[1,2,13,4]
# list1 = [3,14,5,6]
#
# for i in range(20):
#     list.append(random.randint(1,100))
#
# for i in range(20):
#     list1.append(random.randint(1,100))
#
# plt.plot(list)
# plt.plot(list1)
#
# plt.show()

from numpy import *

x = [1.0, 3, 0.1]
y=copy(x)

print(y)
