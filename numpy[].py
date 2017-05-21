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
