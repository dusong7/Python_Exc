# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import cm
# import numpy.fft as fft

#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# u = np.linspace(-1, 1, 100)
# x, y = np.meshgrid(u, u)
# z = x ** 2 + y ** 2
# ax.contourf(x, y, z)
#
#
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.fftpack import fft, ifft
#
# N = 40
# T = 1 / 64.0
#
# x = np.linspace(0, 2*np.pi*N*T, N)
# y1 = np.cos(20*x)
# y2 = np.sin(10*x)
# y3 = np.sin(5*x)
#
# y = y1 + y2 + y3
#
# fy = fft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
# plt.plot(xf, (2.0/N)*np.abs(y[0:N/2]))
# #plt.plot(xf, (2.0/N)*np.abs(fy[0:N/2]))
#
# plt.show()

# x = np.arange(-2*np.pi, 2*np.pi, 0.001)
# y = np.sin(x)
# y1 = np.sin(x) + 0.25*np.sin(3*x)
# fy = fft(y)
# fx = np.linspace(-2*np.pi, 2*np.pi,N/2)
# # plt.scatter(x, y1)
# plt.plot(fx, (2.0/N)*np.abs(fy[0:N/2]))
# x = np.arange(-10,10,1000)
# y = np.sin(x)
#
# a = 10
#
# if a != 1:
#     print a
#     print True
#
#
# plt.show()
# import numpy as np;
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.show()
#
# print ("HH")

# import numpy as np
# import matplotlib.pyplot as plt
#
# X = np.matrix([1.0, 2.0, 3.0, 4.0, 5.0])
#
# print(X)
# import math
# import turtle
# bob = turtle.Turtle();
#
# # print(bob)
# # turtle.mainloop()
# # bob.color("red")
#
# def squral(t, length, angle):
#     for i in range(50):
#         t.fd(length)
#         t.lt(angle)
#
# def circle(t, r):
#     circ = 2 * math.pi * r
#     n = 1
#     length = circ / n
#     squral(t,circ,length)
#
# circle(bob, 10)
# turtle.mainloop()
#
# def newtow(a, x):
#     return (x + a/x)/2
#
#
# for i in range(10):
#     num = newtow(5, 4)
#     newtow(5, num)
#
# print(num)

## newtwen cal sqrt
# x = 8
# a = 8
# y = 8
#
# while True:
#     print(x)
#     y = (x+a/x)/2
#     if x==y:
#         break
#     x = y
#
# import math
# print(math.sqrt(8))

##generate random number and assign to a list
# import random
# RandomTable = []
#
# for i in range(100):
#     RandomTable.append(random.randint(1,10))
#
# print(RandomTable)

# s = 'abc'
# print(type(()))
#<class 'tuple'>

# import dbm  #dbm must is a char or string
# db = dbm.open('cap','c')
#
# for i in range(10):
#     db[''] = random.randint(1,10)
#
# for i in db:
#     print(i,db[i])
# import os
#
# cmd = 'top'
# fp = os.popen(cmd)
#
# print(fp)

class nameInfo:
    def __init__(self):
        print("Name info")
    def name(self, name_):
        print(name_)
    def age(self, age_):
        print(age_)

class emply(nameInfo):
    def __init__(self, names):
        print(self.name(names))

emp = nameInfo()
emp.name('dd')

emp = emply("Test")
#inheritance Test
#http://blog.csdn.net/tclxspy/article/details/51281811
