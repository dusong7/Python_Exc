
import random
import matplotlib.pyplot as plt
list = []

# x = 8
# y = 8
# a = 2

# while True:
#     print(x)
#     list.append(x)
#     y = (x+a/x)/2
#     if(x == y):
#         break
#     x = y
# plt.plot(list)
# plt.show()
list2 = []
file = open("E:/file.txt", "w+")

for i in range(1000000):
    list.append(random.randint(1,1000000))

for i in list:
    list2.append(str(i))

for i in list2:
    file.write(i)
    file.write(" ,")

file.close()
