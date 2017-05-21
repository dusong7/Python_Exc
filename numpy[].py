>>> import numpy as np
>>> z = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
>>> z
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
>>> z[1]
array([5, 6, 7, 8])
>>> z[1:]
array([[ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
>>> z[1:0]
array([], shape=(0, 4), dtype=int64)
>>> z[1:-1]
array([[ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> z[1:-1,1:-1]
array([[ 6,  7],
       [10, 11]])
>>> z[1:-1,1:-1,1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: too many indices for array
>>> z[1:-1,1:-1,1:0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: too many indices for array
>>> z[1:-1,1:]
array([[ 6,  7,  8],
       [10, 11, 12]])
>>> z[1:-1,1:1]
array([], shape=(2, 0), dtype=int64)
>>> z[1:-1,1:2]
array([[ 6],
       [10]])
>>> z[1:-1,1:3]
array([[ 6,  7],
       [10, 11]])
>>> z
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
>>> z[,1]
  File "<stdin>", line 1
    z[,1]
      ^
SyntaxError: invalid syntax
>>> z[,1:]
  File "<stdin>", line 1
    z[,1:]
      ^
SyntaxError: invalid syntax
>>> z[0,1:]
array([2, 3, 4])
>>> z[0]
array([1, 2, 3, 4])
>>> z[,]
  File "<stdin>", line 1
    z[,]
      ^
SyntaxError: invalid syntax
>>> z[:,1]
array([ 2,  6, 10, 14])
>>> z[:]
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
>>> z[:,0]  ## shuchu 列
array([ 1,  5,  9, 13])
>>> 
>>> z[:,-1]
array([ 4,  8, 12, 16])



##[x,y] x 行，y 列[m:n, p:q] 可用负数表示，表示倒数第几个。正着数从0开始
##
