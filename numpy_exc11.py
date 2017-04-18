from numpy import *

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

x = ones((M,N), dtype= 'int32')
print(5*x)

