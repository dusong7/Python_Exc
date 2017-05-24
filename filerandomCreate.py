import io
import sys
import os
import random
import shutil
table = "123456789"

# print(os.listdir("\list1"))

list1 = []
list2 = []
for i in range(1000):
    list = random.sample(table,3)
    open("C://list1//" + "".join(list), 'w')
    list1.append("C://list1//" + "".join(list))

print(os.listdir("C://list1"))

for i in range(1000):
    list = random.sample(table,3)
    open("C://list2//" + "".join(list), 'w')
    list1.append("C://list2//" + "".join(list))
