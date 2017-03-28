import __future__

import cmath
print(cmath.sqrt(-1))

x = [1,4,3,454,5,6]
x.sort()
print(x)
x = ['11', 'fefe', 're344', 'e3433']
x.sort(reverse=True)
print(x)
value = ('12','33')
print(value)
print("%s__%s"%value)
from string import Template
s = Template('$x, glorious $x!')
print(s.substitute(x = 'Sum'))

dic = {"1": "4321", "2":"321"}
##append
dic["3"] = "33"

print(dic)
dic1 = dic.copy()
print(dic1["1"])
# print(type(dic))
