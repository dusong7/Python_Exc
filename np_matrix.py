numpy.matrix

class numpy.matrix[source]
Returns a matrix from an array-like object, or from a string of data. A matrix is a specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as * (matrix multiplication) and ** (matrix power).

Parameters:	
data : array_like or string
If data is a string, it is interpreted as a matrix with commas or spaces separating columns, and semicolons separating rows.
dtype : data-type
Data-type of the output matrix.
copy : bool
If data is already an ndarray, then this flag determines whether the data is copied (the default), or whether a view is constructed.
See also
array

Examples

>>>
>>> a = np.matrix('1 2; 3 4')
>>> print(a)
[[1 2]
 [3 4]]
>>>
>>> np.matrix([[1, 2], [3, 4]])
matrix([[1, 2],
        [3, 4]])
Attributes

A	Return self as an ndarray object.
A1	Return self as a flattened ndarray.
H	Returns the (complex) conjugate transpose of self.
I	Returns the (multiplicative) inverse of invertible self.
T	Returns the transpose of the matrix.
base	Base object if memory is from some other object.
ctypes	An object to simplify the interaction of the array with the ctypes module.
data	Python buffer object pointing to the start of the array’s data.
dtype	Data-type of the array’s elements.
flags	Information about the memory layout of the array.
flat	A 1-D iterator over the array.
imag	The imaginary part of the array.
itemsize	Length of one array element in bytes.
nbytes	Total bytes consumed by the elements of the array.
ndim	Number of array dimensions.
real	The real part of the array.
shape	Tuple of array dimensions.
size	Number of elements in the array.
strides	Tuple of bytes to step in each dimension when traversing an array.
Methods

all([axis, out])	Test whether all matrix elements along a given axis evaluate to True.
any([axis, out])	Test whether any array element along a given axis evaluates to True.
argmax([axis, out])	Indexes of the maximum values along an axis.
argmin([axis, out])	Indexes of the minimum values along an axis.
argpartition(kth[, axis, kind, order])	Returns the indices that would partition this array.
argsort([axis, kind, order])	Returns the indices that would sort this array.
astype(dtype[, order, casting, subok, copy])	Copy of the array, cast to a specified type.
byteswap(inplace)	Swap the bytes of the array elements
choose(choices[, out, mode])	Use an index array to construct a new array from a set of choices.
clip([min, max, out])	Return an array whose values are limited to [min, max].
compress(condition[, axis, out])	Return selected slices of this array along given axis.
conj()	Complex-conjugate all elements.
conjugate()	Return the complex conjugate, element-wise.
copy([order])	Return a copy of the array.
cumprod([axis, dtype, out])	Return the cumulative product of the elements along the given axis.
cumsum([axis, dtype, out])	Return the cumulative sum of the elements along the given axis.
diagonal([offset, axis1, axis2])	Return specified diagonals.
dot(b[, out])	Dot product of two arrays.
dump(file)	Dump a pickle of the array to the specified file.
dumps()	Returns the pickle of the array as a string.
fill(value)	Fill the array with a scalar value.
flatten([order])	Return a flattened copy of the matrix.
getA()	Return self as an ndarray object.
getA1()	Return self as a flattened ndarray.
getH()	Returns the (complex) conjugate transpose of self.
getI()	Returns the (multiplicative) inverse of invertible self.
getT()	Returns the transpose of the matrix.
getfield(dtype[, offset])	Returns a field of the given array as a certain type.
item(*args)	Copy an element of an array to a standard Python scalar and return it.
itemset(*args)	Insert scalar into an array (scalar is cast to array’s dtype, if possible)
max([axis, out])	Return the maximum value along an axis.
mean([axis, dtype, out])	Returns the average of the matrix elements along the given axis.
min([axis, out])	Return the minimum value along an axis.
newbyteorder([new_order])	Return the array with the same data viewed with a different byte order.
nonzero()	Return the indices of the elements that are non-zero.
partition(kth[, axis, kind, order])	Rearranges the elements in the array in such a way that value of the element in kth position is in the position it would be in a sorted array.
prod([axis, dtype, out])	Return the product of the array elements over the given axis.
ptp([axis, out])	Peak-to-peak (maximum - minimum) value along the given axis.
put(indices, values[, mode])	Set a.flat[n] = values[n] for all n in indices.
ravel([order])	Return a flattened matrix.
repeat(repeats[, axis])	Repeat elements of an array.
reshape(shape[, order])	Returns an array containing the same data with a new shape.
resize(new_shape[, refcheck])	Change shape and size of array in-place.
round([decimals, out])	Return a with each element rounded to the given number of decimals.
searchsorted(v[, side, sorter])	Find indices where elements of v should be inserted in a to maintain order.
setfield(val, dtype[, offset])	Put a value into a specified place in a field defined by a data-type.
setflags([write, align, uic])	Set array flags WRITEABLE, ALIGNED, and UPDATEIFCOPY, respectively.
sort([axis, kind, order])	Sort an array, in-place.
squeeze([axis])	Return a possibly reshaped matrix.
std([axis, dtype, out, ddof])	Return the standard deviation of the array elements along the given axis.
sum([axis, dtype, out])	Returns the sum of the matrix elements, along the given axis.
swapaxes(axis1, axis2)	Return a view of the array with axis1 and axis2 interchanged.
take(indices[, axis, out, mode])	Return an array formed from the elements of a at the given indices.
tobytes([order])	Construct Python bytes containing the raw data bytes in the array.
tofile(fid[, sep, format])	Write array to a file as text or binary (default).
tolist()	Return the matrix as a (possibly nested) list.
tostring([order])	Construct Python bytes containing the raw data bytes in the array.
trace([offset, axis1, axis2, dtype, out])	Return the sum along diagonals of the array.
transpose(*axes)	Returns a view of the array with axes transposed.
var([axis, dtype, out, ddof])	Returns the variance of the matrix elements, along the given axis.
view([dtype, type])	New view of array with the same data.



numpy模块中的矩阵对象为numpy.matrix，包括矩阵数据的处理，矩阵的计算，以及基本的统计功能，转置，可逆性等等，包括对复数的处理，均在matrix对象中。 class numpy.matrix(data,dtype,copy):返回一个矩阵，其中data为ndarray对象或者字符形式；dtype:为data的type；copy:为bool类型。

>>> a = np.matrix('1 2 7; 3 4 8; 5 6 9')
>>> a             #矩阵的换行必须是用分号(;)隔开，内部数据必须为字符串形式(‘ ’)，矩
matrix([[1, 2, 7],       #阵的元素之间必须以空格隔开。
[3, 4, 8],
[5, 6, 9]])

>>> b=np.array([[1,5],[3,2]])
>>> x=np.matrix(b)   #矩阵中的data可以为数组对象。
>>> x
matrix([[1, 5],
[3, 2]])
矩阵对象的属性：

matrix.T transpose：返回矩阵的转置矩阵
matrix.H hermitian (conjugate) transpose：返回复数矩阵的共轭元素矩阵
matrix.I inverse：返回矩阵的逆矩阵
matrix.A base array：返回矩阵基于的数组
矩阵对象的方法：
all([axis, out]) :沿给定的轴判断矩阵所有元素是否为真(非0即为真)
any([axis, out]) :沿给定轴的方向判断矩阵元素是否为真，只要一个元素为真则为真。
argmax([axis, out]) :沿给定轴的方向返回最大元素的索引（最大元素的位置）.
argmin([axis, out]): 沿给定轴的方向返回最小元素的索引（最小元素的位置）
argsort([axis, kind, order]) :返回排序后的索引矩阵
astype(dtype[, order, casting, subok, copy]):将该矩阵数据复制，且数据类型为指定的数据类型
byteswap(inplace) Swap the bytes of the array elements
choose(choices[, out, mode]) :根据给定的索引得到一个新的数据矩阵（索引从choices给定）
clip(a_min, a_max[, out]) :返回新的矩阵，比给定元素大的元素为a_max，小的为a_min
compress(condition[, axis, out]) :返回满足条件的矩阵
conj() :返回复数的共轭复数
conjugate() :返回所有复数的共轭复数元素
copy([order]) :复制一个矩阵并赋给另外一个对象，b=a.copy()
cumprod([axis, dtype, out]) :返回沿指定轴的元素累积矩阵
cumsum([axis, dtype, out]) :返回沿指定轴的元素累积和矩阵
diagonal([offset, axis1, axis2]) :返回矩阵中对角线的数据
dot(b[, out]) :两个矩阵的点乘
dump(file) :将矩阵存储为指定文件,可以通过pickle.loads()或者numpy.loads()如:a.dump(‘d:\\a.txt’)
dumps() :将矩阵的数据转存为字符串.
fill(value) :将矩阵中的所有元素填充为指定的value
flatten([order]) :将矩阵转化为一个一维的形式，但是还是matrix对象
getA() :返回自己，但是作为ndarray返回
getA1()：返回一个扁平（一维）的数组（ndarray）
getH() :返回自身的共轭复数转置矩阵
getI() :返回本身的逆矩阵
getT() :返回本身的转置矩阵
max([axis, out]) ：返回指定轴的最大值
mean([axis, dtype, out]) :沿给定轴方向，返回其均值
min([axis, out]) ：返回指定轴的最小值
nonzero() :返回非零元素的索引矩阵
prod([axis, dtype, out]) :返回指定轴方型上，矩阵元素的乘积.
ptp([axis, out]) :返回指定轴方向的最大值减去最小值.
put(indices, values[, mode]) :用给定的value替换矩阵本身给定索引（indices）位置的值
ravel([order]) :返回一个数组，该数组是一维数组或平数组
repeat(repeats[, axis]) :重复矩阵中的元素，可以沿指定轴方向重复矩阵元素，repeats为重复次数
reshape(shape[, order]) :改变矩阵的大小,如：reshape([2,3])
resize(new_shape[, refcheck]) :改变该数据的尺寸大小
round([decimals, out]) :返回指定精度后的矩阵，指定的位数采用四舍五入，若为1，则保留一位小数
searchsorted(v[, side, sorter]) :搜索V在矩阵中的索引位置
sort([axis, kind, order]) :对矩阵进行排序或者按轴的方向进行排序
squeeze([axis]) :移除长度为1的轴
std([axis, dtype, out, ddof]) :沿指定轴的方向，返回元素的标准差.
sum([axis, dtype, out]) ：沿指定轴的方向，返回其元素的总和
swapaxes(axis1, axis2):交换两个轴方向上的数据.
take(indices[, axis, out, mode]) :提取指定索引位置的数据,并以一维数组或者矩阵返回(主要取决axis)
tofile(fid[, sep, format]) :将矩阵中的数据以二进制写入到文件
tolist() :将矩阵转化为列表形式
tostring([order]):将矩阵转化为python的字符串.
trace([offset, axis1, axis2, dtype, out]):返回对角线元素之和
transpose(*axes) :返回矩阵的转置矩阵，不改变原有矩阵
var([axis, dtype, out, ddof]) ：沿指定轴方向，返回矩阵元素的方差
view([dtype, type]) :生成一个相同数据，但是类型为指定新类型的矩阵。
ü  All方法

>>> a = np.asmatrix('0 2 7; 3 4 8; 5 0 9')
>>> a.all()
False
>>> a.all(axis=0)
matrix([[False, False,  True]], dtype=bool)
>>> a.all(axis=1)
matrix([[False],
[ True],
[False]], dtype=bool)

ü  Astype方法
>>> a.astype(float)
matrix([[ 12.,   3.,   5.],
[ 32.,  23.,   9.],
[ 10., -14.,  78.]])

ü  Argsort方法
>>> a=np.matrix('12 3 5; 32 23 9; 10 -14 78')
>>> a.argsort()
matrix([[1, 2, 0],
[2, 1, 0],
[1, 0, 2]])

ü  Clip方法
>>> a
matrix([[ 12,   3,   5],
[ 32,  23,   9],
[ 10, -14,  78]])
>>> a.clip(12,32)
matrix([[12, 12, 12],
[32, 23, 12],
[12, 12, 32]])

ü  Cumprod方法
>>> a.cumprod(axis=1)
matrix([[    12,     36,    180],
[    32,    736,   6624],
[    10,   -140, -10920]])

ü  Cumsum方法
>>> a.cumsum(axis=1)
matrix([[12, 15, 20],
[32, 55, 64],
[10, -4, 74]])

ü  Tolist方法
>>> b.tolist()
[[12, 3, 5], [32, 23, 9], [10, -14, 78]]

ü  Tofile方法
>>> b.tofile('d:\\b.txt')

ü  compress()方法
>>> from numpy import *
>>> a = array([10, 20, 30, 40])
>>> condition = (a > 15) & (a < 35)
>>> condition
array([False, True, True, False], dtype=bool)
>>> a.compress(condition)
array([20, 30])
>>> a[condition]                                      # same effect
array([20, 30])
>>> compress(a >= 30, a)                              # this form a
so exists
array([30, 40])
>>> b = array([[10,20,30],[40,50,60]])
>>> b.compress(b.ravel() >= 22)
array([30, 40, 50, 60])
>>> x = array([3,1,2])
>>> y = array([50, 101])
>>> b.compress(x >= 2, axis=1)                       # illustrates 
the use of the axis keyword
array([[10, 30],
[40, 60]])
>>> b.compress(y >= 100, axis=0)
array([[40, 50, 60]])

This is an archival dump of old wiki content --- see scipy.org for current material.
Please see https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
SciPy Tentative_NumPy_Tutorial
Attachments
Please do not hesitate to click the edit button. You will need to create a User Account first.

Contents
Prerequisites
The Basics
An example
Array Creation
Printing Arrays
Basic Operations
Universal Functions
Indexing, Slicing and Iterating
Shape Manipulation
Changing the shape of an array
Stacking together different arrays
Splitting one array into several smaller ones
Copies and Views
No Copy at All
View or Shallow Copy
Deep Copy
Functions and Methods Overview
Less Basic
Broadcasting rules
Fancy indexing and index tricks
Indexing with Arrays of Indices
Indexing with Boolean Arrays
The ix_() function
Indexing with strings
Linear Algebra
Simple Array Operations
The Matrix Class
Indexing: Comparing Matrices and 2D Arrays
Tricks and Tips
"Automatic" Reshaping
Vector Stacking
Histograms
References
 
Prerequisites

Before reading this tutorial you should know a bit of Python. If you would like to refresh your memory, take a look at the Python tutorial.

If you wish to work the examples in this tutorial, you must also have some software installed on your computer. Minimally:

Python
NumPy
These you may find useful:

ipython is an enhanced interactive Python shell which is very convenient for exploring NumPy's features
matplotlib will enable you to plot graphics
SciPy provides a lot of scientific routines that work on top of NumPy
The Basics

NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In Numpy dimensions are called axes. The number of axes is rank.

For example, the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1, because it has one axis. That axis has a length of 3. In example pictured below, the array has rank 2 (it is 2-dimensional). The first dimension (axis) has a length of 2, the second dimension has a length of 3.


[[ 1., 0., 0.],
 [ 0., 1., 2.]]
Numpy's array class is called ndarray. It is also known by the alias array. Note that numpy.array is not the same as the Standard Python Library class array.array, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an ndarray object are:

ndarray.ndim
the number of axes (dimensions) of the array. In the Python world, the number of dimensions is referred to as rank.
ndarray.shape
the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the rank, or number of dimensions, ndim.
ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.
ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtype's using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
ndarray.data
the buffer containing the actual elements of the array. Normally, we won't need to use this attribute because we will access the elements in an array using indexing facilities.
An example


>>> from numpy  import *
>>> a = arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int32'
>>> a.itemsize
4
>>> a.size
15
>>> type(a)
numpy.ndarray
>>> b = array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
numpy.ndarray
Array Creation

There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using the array function. The type of the resulting array is deduced from the type of the elements in the sequences.


>>> from numpy import *
>>> a = array( [2,3,4] )
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int32')
>>> b = array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
A frequent error consists in calling array with multiple numeric arguments, rather than providing a single list of numbers as an argument.

>>> a = array(1,2,3,4)    # WRONG

>>> a = array([1,2,3,4])  # RIGHT
array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.


>>> b = array( [ (1.5,2,3), (4,5,6) ] )
>>> b
array([[ 1.5,  2. ,  3. ],
       [ 4. ,  5. ,  6. ]])
The type of the array can also be explicitly specified at creation time:

>>> c = array( [ [1,2], [3,4] ], dtype=complex )
>>> c
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])
Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.

The function zeros creates an array full of zeros, the function ones creates an array full of ones, and the function empty creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is float64.

>>> zeros( (3,4) )
array([[0.,  0.,  0.,  0.],
       [0.,  0.,  0.,  0.],
       [0.,  0.,  0.,  0.]])
>>> ones( (2,3,4), dtype=int16 )                # dtype can also be specified
array([[[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]],
       [[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]]], dtype=int16)
>>> empty( (2,3) )
array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
       [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])
To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists


>>> arange( 10, 30, 5 )
array([10, 15, 20, 25])
>>> arange( 0, 2, 0.3 )                 # it accepts float arguments
array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function linspace that receives as an argument the number of elements that we want, instead of the step:


>>> linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
>>> x = linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
>>> f = sin(x)
See also
array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, rand, randn, fromfunction, fromfile
Printing Arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:

the last axis is printed from left to right,
the second-to-last is printed from top to bottom,
the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.


>>> a = arange(6)                         # 1d array
>>> print a
[0 1 2 3 4 5]
>>>
>>> b = arange(12).reshape(4,3)           # 2d array
>>> print b
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = arange(24).reshape(2,3,4)         # 3d array
>>> print c
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
See below to get more details on reshape.

If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:


>>> print arange(10000)
[   0    1    2 ..., 9997 9998 9999]
>>>
>>> print arange(10000).reshape(100,100)
[[   0    1    2 ...,   97   98   99]
 [ 100  101  102 ...,  197  198  199]
 [ 200  201  202 ...,  297  298  299]
 ...,
 [9700 9701 9702 ..., 9797 9798 9799]
 [9800 9801 9802 ..., 9897 9898 9899]
 [9900 9901 9902 ..., 9997 9998 9999]]
To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.


>>> set_printoptions(threshold='nan')
Basic Operations

Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.


>>> a = array( [20,30,40,50] )
>>> b = arange( 4 )
>>> b
array([0, 1, 2, 3])
>>> c = a-b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10*sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a<35
array([True, True, False, False], dtype=bool)
Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. The matrix product can be performed using the dot function or creating matrix objects ( see matrix section of this tutorial ).

>>> A = array( [[1,1],
...             [0,1]] )
>>> B = array( [[2,0],
...             [3,4]] )
>>> A*B                         # elementwise product
array([[2, 0],
       [0, 4]])
>>> dot(A,B)                    # matrix product
array([[5, 4],
       [3, 4]])
Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.


>>> a = ones((2,3), dtype=int)
>>> b = random.random((2,3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[ 3.69092703,  3.8324276 ,  3.0114541 ],
       [ 3.18679111,  3.3039349 ,  3.37600289]])
>>> a += b                                  # b is converted to integer type
>>> a
array([[6, 6, 6],
       [6, 6, 6]])
When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).


>>> a = ones(3, dtype=int32)
>>> b = linspace(0,pi,3)
>>> b.dtype.name
'float64'
>>> c = a+b
>>> c
array([ 1.        ,  2.57079633,  4.14159265])
>>> c.dtype.name
'float64'
>>> d = exp(c*1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.


>>> a = random.random((2,3))
>>> a
array([[ 0.6903007 ,  0.39168346,  0.16524769],
       [ 0.48819875,  0.77188505,  0.94792155]])
>>> a.sum()
3.4552372100521485
>>> a.min()
0.16524768654743593
>>> a.max()
0.9479215542670073
By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the axis parameter you can apply an operation along the specified axis of an array:


>>> b = arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)                            # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)                            # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)                         # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
Universal Functions

NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called "universal functions"(ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.


>>> B = arange(3)
>>> B
array([0, 1, 2])
>>> exp(B)
array([ 1.        ,  2.71828183,  7.3890561 ])
>>> sqrt(B)
array([ 0.        ,  1.        ,  1.41421356])
>>> C = array([2., -1., 4.])
>>> add(B, C)
array([ 2.,  0.,  6.])
See also
all, alltrue, any, apply along axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, conjugate, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sometrue, sort, std, sum, trace, transpose, var, vdot, vectorize, where
Indexing, Slicing and Iterating

One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.


>>> a = arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
>>> a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
>>> a[ : :-1]                                 # reversed a
array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
>>> for i in a:
...         print i**(1/3.),
...
nan 1.0 nan 3.0 nan 5.0 6.0 7.0 8.0 9.0
Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:


>>> def f(x,y):
...         return 10*x+y
...
>>> b = fromfunction(f,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[0:5, 1]                       # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[ : ,1]                        # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, : ]                      # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
When fewer indices are provided than the number of axes, the missing indices are considered complete slices:


>>> b[-1]                                  # the last row. Equivalent to b[-1,:]
array([40, 41, 42, 43])
The expression within brackets in b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write this using dots as b[i,...].

The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is a rank 5 array (i.e., it has 5 axes), then

x[1,2,...] is equivalent to x[1,2,:,:,:],
x[...,3] to x[:,:,:,:,3] and
x[4,...,5,:] to x[4,:,:,5,:].

>>> c = array( [ [[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
...               [ 10, 12, 13]],
...
...              [[100,101,102],
...               [110,112,113]] ] )
>>> c.shape
(2, 2, 3)
>>> c[1,...]                                   # same as c[1,:,:] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[...,2]                                   # same as c[:,:,2]
array([[  2,  13],
       [102, 113]])
Iterating over multidimensional arrays is done with respect to the first axis:


>>> for row in b:
...         print row
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
However, if one wants to perform an operation on each element in the array, one can use the flat attribute which is an iterator over all the elements of the array:


>>> for element in b.flat:
...         print element,
...
0 1 2 3 10 11 12 13 20 21 22 23 30 31 32 33 40 41 42 43
See also
[], ..., newaxis, ndenumerate, indices, index exp

Shape Manipulation

Changing the shape of an array

An array has a shape given by the number of elements along each axis:


>>> a = floor(10*random.random((3,4)))
>>> a
array([[ 7.,  5.,  9.,  3.],
       [ 7.,  2.,  7.,  8.],
       [ 6.,  8.,  3.,  2.]])
>>> a.shape
(3, 4)
The shape of an array can be changed with various commands:


>>> a.ravel() # flatten the array
array([ 7.,  5.,  9.,  3.,  7.,  2.,  7.,  8.,  6.,  8.,  3.,  2.])
>>> a.shape = (6, 2)
>>> a.transpose()
array([[ 7.,  9.,  7.,  7.,  6.,  3.],
       [ 5.,  3.,  2.,  8.,  8.,  2.]])
The order of the elements in the array resulting from ravel() is normally "C-style", that is, the rightmost index "changes the fastest", so the element after a[0,0] is a[0,1]. If the array is reshaped to some other shape, again the array is treated as "C-style". Numpy normally creates arrays stored in this order, so ravel() will usually not need to copy its argument, but if the array was made by taking slices of another array or created with unusual options, it may need to be copied. The functions ravel() and reshape() can also be instructed, using an optional argument, to use FORTRAN-style arrays, in which the leftmost index changes the fastest.

The reshape function returns its argument with a modified shape, whereas the resize method modifies the array itself:


>>> a
array([[ 7.,  5.],
       [ 9.,  3.],
       [ 7.,  2.],
       [ 7.,  8.],
       [ 6.,  8.],
       [ 3.,  2.]])
>>> a.resize((2,6))
>>> a
array([[ 7.,  5.,  9.,  3.,  7.,  2.],
       [ 7.,  8.,  6.,  8.,  3.,  2.]])
If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:


>>> a.reshape(3,-1)
array([[ 7.,  5.,  9.,  3.],
       [ 7.,  2.,  7.,  8.],
       [ 6.,  8.,  3.,  2.]])
See also:: shape example, reshape example, resize example, ravel example

Stacking together different arrays

Several arrays can be stacked together along different axes:


>>> a = floor(10*random.random((2,2)))
>>> a
array([[ 1.,  1.],
       [ 5.,  8.]])
>>> b = floor(10*random.random((2,2)))
>>> b
array([[ 3.,  3.],
       [ 6.,  0.]])
>>> vstack((a,b))
array([[ 1.,  1.],
       [ 5.,  8.],
       [ 3.,  3.],
       [ 6.,  0.]])
>>> hstack((a,b))
array([[ 1.,  1.,  3.,  3.],
       [ 5.,  8.,  6.,  0.]])
The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to vstack only for 1D arrays:


>>> column_stack((a,b))   # With 2D arrays
array([[ 1.,  1.,  3.,  3.],
       [ 5.,  8.,  6.,  0.]])
>>> a=array([4.,2.])
>>> b=array([2.,8.])
>>> a[:,newaxis]  # This allows to have a 2D columns vector
array([[ 4.],
       [ 2.]])
>>> column_stack((a[:,newaxis],b[:,newaxis]))
array([[ 4.,  2.],
       [ 2.,  8.]])
>>> vstack((a[:,newaxis],b[:,newaxis])) # The behavior of vstack is different
array([[ 4.],
       [ 2.],
       [ 2.],
       [ 8.]])
The function row_stack, on the other hand, stacks 1D arrays as rows into a 2D array.

For arrays of with more than two dimensions, hstack stacks along their second axes, vstack stacks along their first axes, and concatenate allows for an optional arguments giving the number of the axis along which the concatenation should happen.

Note

In complex cases, r_[] and c_[] are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals (":") :

>>> r_[1:4,0,4]
array([1, 2, 3, 0, 4])
When used with arrays as arguments, r_[] and c_[] are similar to vstack and hstack in their default behavior, but allow for an optional argument giving the number of the axis along which to concatenate.

See also: hstack example, vstack exammple, column_stack example, row_stack example, concatenate example, c_ example, r_ example

Splitting one array into several smaller ones

Using hsplit, you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur:


>>> a = floor(10*random.random((2,12)))
>>> a
array([[ 8.,  8.,  3.,  9.,  0.,  4.,  3.,  0.,  0.,  6.,  4.,  4.],
       [ 0.,  3.,  2.,  9.,  6.,  0.,  4.,  5.,  7.,  5.,  1.,  4.]])
>>> hsplit(a,3)   # Split a into 3
[array([[ 8.,  8.,  3.,  9.],
       [ 0.,  3.,  2.,  9.]]), array([[ 0.,  4.,  3.,  0.],
       [ 6.,  0.,  4.,  5.]]), array([[ 0.,  6.,  4.,  4.],
       [ 7.,  5.,  1.,  4.]])]
>>> hsplit(a,(3,4))   # Split a after the third and the fourth column
[array([[ 8.,  8.,  3.],
       [ 0.,  3.,  2.]]), array([[ 9.],
       [ 9.]]), array([[ 0.,  4.,  3.,  0.,  0.,  6.,  4.,  4.],
       [ 6.,  0.,  4.,  5.,  7.,  5.,  1.,  4.]])]
vsplit splits along the vertical axis, and array split allows one to specify along which axis to split.

Copies and Views

When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

No Copy at All

Simple assignments make no copy of array objects or of their data.


>>> a = arange(12)
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True
>>> b.shape = 3,4    # changes the shape of a
>>> a.shape
(3, 4)
Python passes mutable objects as references, so function calls make no copy.


>>> def f(x):
...     print id(x)
...
>>> id(a)                           # id is a unique identifier of an object
148293216
>>> f(a)
148293216
View or Shallow Copy

Different array objects can share the same data. The view method creates a new array object that looks at the same data.


>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c.shape = 2,6                      # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0,4] = 1234                      # a's data changes
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
Slicing an array returns a view of it:


>>> s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
>>> s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
Deep Copy

The copy method makes a complete copy of the array and its data.


>>> d = a.copy()                          # a new array object with new data is created
>>> d is a
False
>>> d.base is a                           # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
Functions and Methods Overview

Here is a list of NumPy functions and methods names ordered in some categories. The names link to the Numpy_Example_List so that you can see the functions in action.

Array Creation
arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
Conversions
astype, atleast 1d, atleast 2d, atleast 3d, mat
Manipulations
array split, column stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
Questions
all, any, nonzero, where
Ordering
argmax, argmin, argsort, max, min, ptp, searchsorted, sort
Operations
choose, compress, cumprod, cumsum, inner, fill, imag, prod, put, putmask, real, sum
Basic Statistics
cov, mean, std, var
Basic Linear Algebra
cross, dot, outer, svd, vdot
Less Basic

Broadcasting rules

Broadcasting allows universal functions to deal in a meaningful way with inputs that do not have exactly the same shape.

The first rule of broadcasting is that if all input arrays do not have the same number of dimensions, a "1" will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.

The second rule of broadcasting ensures that arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the "broadcast" array.

After application of the broadcasting rules, the sizes of all arrays must match. More details can be found in this documentation.

Fancy indexing and index tricks

NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, as we saw before, arrays can be indexed by arrays of integers and arrays of booleans.

Indexing with Arrays of Indices


>>> a = arange(12)**2                          # the first 12 square numbers
>>> i = array( [ 1,1,3,8,5 ] )                 # an array of indices
>>> a[i]                                       # the elements of a at the positions i
array([ 1,  1,  9, 64, 25])
>>>
>>> j = array( [ [ 3, 4], [ 9, 7 ] ] )         # a bidimensional array of indices
>>> a[j]                                       # the same shape as j
array([[ 9, 16],
       [81, 49]])
When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a. The following example shows this behavior by converting an image of labels into a color image using a palette.


>>> palette = array( [ [0,0,0],                # black
...                    [255,0,0],              # red
...                    [0,255,0],              # green
...                    [0,0,255],              # blue
...                    [255,255,255] ] )       # white
>>> image = array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
...                  [ 0, 3, 4, 0 ]  ] )
>>> palette[image]                            # the (2,4,3) color image
array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],
       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.


>>> a = arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = array( [ [0,1],                        # indices for the first dim of a
...              [1,2] ] )
>>> j = array( [ [2,1],                        # indices for the second dim
...              [3,3] ] )
>>>
>>> a[i,j]                                     # i and j must have equal shape
array([[ 2,  5],
       [ 7, 11]])
>>>
>>> a[i,2]
array([[ 2,  6],
       [ 6, 10]])
>>>
>>> a[:,j]                                     # i.e., a[ : , j]
array([[[ 2,  1],
        [ 3,  3]],
       [[ 6,  5],
        [ 7,  7]],
       [[10,  9],
        [11, 11]]])
Naturally, we can put i and j in a sequence (say a list) and then do the indexing with the list.


>>> l = [i,j]
>>> a[l]                                       # equivalent to a[i,j]
array([[ 2,  5],
       [ 7, 11]])
However, we can not do this by putting i and j into an array, because this array will be interpreted as indexing the first dimension of a.


>>> s = array( [i,j] )
>>> a[s]                                       # not what we want
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: index (3) out of range (0<=index<=2) in dimension 0
>>>
>>> a[tuple(s)]                                # same as a[i,j]
array([[ 2,  5],
       [ 7, 11]])
Another common use of indexing with arrays is the search of the maximum value of time-dependent series :


>>> time = linspace(20, 145, 5)                 # time scale
>>> data = sin(arange(20)).reshape(5,4)         # 4 time-dependent series
>>> time
array([  20.  ,   51.25,   82.5 ,  113.75,  145.  ])
>>> data
array([[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
       [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
       [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
       [-0.28790332, -0.96139749, -0.75098725,  0.14987721]])
>>>
>>> ind = data.argmax(axis=0)                   # index of the maxima for each series
>>> ind
array([2, 0, 3, 1])
>>>
>>> time_max = time[ ind]                       # times corresponding to the maxima
>>>
>>> data_max = data[ind, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
>>>
>>> time_max
array([  82.5 ,   20.  ,  113.75,   51.25])
>>> data_max
array([ 0.98935825,  0.84147098,  0.99060736,  0.6569866 ])
>>>
>>> all(data_max == data.max(axis=0))
True
You can also use indexing with arrays as a target to assign to:


>>> a = arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a[[1,3,4]] = 0
>>> a
array([0, 0, 2, 0, 0])
However, when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value:


>>> a = arange(5)
>>> a[[0,0,2]]=[1,2,3]
>>> a
array([2, 1, 3, 3, 4])
This is reasonable enough, but watch out if you want to use Python's += construct, as it may not do what you expect:


>>> a = arange(5)
>>> a[[0,0,2]]+=1
>>> a
array([1, 1, 3, 3, 4])
Even though 0 occurs twice in the list of indices, the 0th element is only incremented once. This is because Python requires "a+=1" to be equivalent to "a=a+1".

Indexing with Boolean Arrays

When we index arrays with arrays of (integer) indices we are providing the list of indices to pick. With boolean indices the approach is different; we explicitly choose which items in the array we want and which ones we don't.

The most natural way one can think of for boolean indexing is to use boolean arrays that have the same shape as the original array:


>>> a = arange(12).reshape(3,4)
>>> b = a > 4
>>> b                                          # b is a boolean with a's shape
array([[False, False, False, False],
       [False, True, True, True],
       [True, True, True, True]], dtype=bool)
>>> a[b]                                       # 1d array with the selected elements
array([ 5,  6,  7,  8,  9, 10, 11])
This property can be very useful in assignments:


>>> a[b] = 0                                   # All elements of 'a' higher than 4 become 0
>>> a
array([[0, 1, 2, 3],
       [4, 0, 0, 0],
       [0, 0, 0, 0]])
You can look at the Mandelbrot set example to see how to use boolean indexing to generate an image of the Mandelbrot set.

The second way of indexing with booleans is more similar to integer indexing; for each dimension of the array we give a 1D boolean array selecting the slices we want.


>>> a = arange(12).reshape(3,4)
>>> b1 = array([False,True,True])             # first dim selection
>>> b2 = array([True,False,True,False])       # second dim selection
>>>
>>> a[b1,:]                                   # selecting rows
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[b1]                                     # same thing
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[:,b2]                                   # selecting columns
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10]])
>>>
>>> a[b1,b2]                                  # a weird thing to do
array([ 4, 10])
Note that the length of the 1D boolean array must coincide with the length of the dimension (or axis) you want to slice. In the previous example, b1 is a 1-rank array with length 3 (the number of rows in a), and b2 (of length 4) is suitable to index the 2nd rank (columns) of a.

The ix_() function

The ix_ function can be used to combine different vectors so as to obtain the result for each n-uplet. For example, if you want to compute all the a+b*c for all the triplets taken from each of the vectors a, b and c:


>>> a = array([2,3,4,5])
>>> b = array([8,5,4])
>>> c = array([5,4,6,8,3])
>>> ax,bx,cx = ix_(a,b,c)
>>> ax
array([[[2]],

       [[3]],

       [[4]],

       [[5]]])
>>> bx
array([[[8],
        [5],
        [4]]])
>>> cx
array([[[5, 4, 6, 8, 3]]])
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
>>> result = ax+bx*cx
>>> result
array([[[42, 34, 50, 66, 26],
        [27, 22, 32, 42, 17],
        [22, 18, 26, 34, 14]],
       [[43, 35, 51, 67, 27],
        [28, 23, 33, 43, 18],
        [23, 19, 27, 35, 15]],
       [[44, 36, 52, 68, 28],
        [29, 24, 34, 44, 19],
        [24, 20, 28, 36, 16]],
       [[45, 37, 53, 69, 29],
        [30, 25, 35, 45, 20],
        [25, 21, 29, 37, 17]]])
>>> result[3,2,4]
17
>>> a[3]+b[2]*c[4]
17
You could also implement the reduce as follows:


def ufunc_reduce(ufct, *vectors):
    vs = ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r,v)
    return r
and then use it as:


>>> ufunc_reduce(add,a,b,c)
array([[[15, 14, 16, 18, 13],
        [12, 11, 13, 15, 10],
        [11, 10, 12, 14,  9]],
       [[16, 15, 17, 19, 14],
        [13, 12, 14, 16, 11],
        [12, 11, 13, 15, 10]],
       [[17, 16, 18, 20, 15],
        [14, 13, 15, 17, 12],
        [13, 12, 14, 16, 11]],
       [[18, 17, 19, 21, 16],
        [15, 14, 16, 18, 13],
        [14, 13, 15, 17, 12]]])
The advantage of this version of reduce compared to the normal ufunc.reduce is that it makes use of the Broadcasting Rules in order to avoid creating an argument array the size of the output times the number of vectors.

Indexing with strings

See RecordArrays.

Linear Algebra

Work in progress. Basic linear algebra to be included here.

Simple Array Operations

See linalg.py in numpy folder for more.

>>> from numpy import *
>>> from numpy.linalg import *

>>> a = array([[1.0, 2.0], [3.0, 4.0]])
>>> print a
[[ 1.  2.]
 [ 3.  4.]]

>>> a.transpose()
array([[ 1.,  3.],
       [ 2.,  4.]])

>>> inv(a)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

>>> u = eye(2) # unit 2x2 matrix; "eye" represents "I"
>>> u
array([[ 1.,  0.],
       [ 0.,  1.]])
>>> j = array([[0.0, -1.0], [1.0, 0.0]])

>>> dot (j, j) # matrix product
array([[-1.,  0.],
       [ 0., -1.]])

>>> trace(u)  # trace
2.0

>>> y = array([[5.], [7.]])
>>> solve(a, y)
array([[-3.],
       [ 4.]])

>>> eig(j)
(array([ 0.+1.j,  0.-1.j]),
array([[ 0.70710678+0.j,  0.70710678+0.j],
       [ 0.00000000-0.70710678j,  0.00000000+0.70710678j]]))
Parameters:
    square matrix

Returns
    The eigenvalues, each repeated according to its multiplicity.

    The normalized (unit "length") eigenvectors, such that the
    column ``v[:,i]`` is the eigenvector corresponding to the
    eigenvalue ``w[i]`` .
The Matrix Class

Here is a short intro to the Matrix class.


>>> A = matrix('1.0 2.0; 3.0 4.0')
>>> A
[[ 1.  2.]
 [ 3.  4.]]
>>> type(A)  # file where class is defined
<class 'numpy.matrixlib.defmatrix.matrix'>

>>> A.T  # transpose
[[ 1.  3.]
 [ 2.  4.]]

>>> X = matrix('5.0 7.0')
>>> Y = X.T
>>> Y
[[5.]
 [7.]]

>>> print A*Y  # matrix multiplication
[[19.]
 [43.]]

>>> print A.I  # inverse
[[-2.   1. ]
 [ 1.5 -0.5]]

>>> solve(A, Y)  # solving linear equation
matrix([[-3.],
        [ 4.]])
Indexing: Comparing Matrices and 2D Arrays

Note that there are some important differences between NumPy arrays and matrices. NumPy provides two fundamental objects: an N-dimensional array object and a universal function object. Other objects are built on top of these. In particular, matrices are 2-dimensional array objects that inherit from the NumPy array object. For both arrays and matrices, indices must consist of a proper combination of one or more of the following: integer scalars, ellipses, a list of integers or boolean values, a tuple of integers or boolean values, and a 1-dimensional array of integer or boolean values. A matrix can be used as an index for matrices, but commonly an array, list, or other form is needed to accomplish a given task.

As usual in Python, indexing is zero-based. Traditionally we represent a 2D array or matrix as a rectangular array of rows and columns, where movement along axis 0 is movement across rows, while movement along axis 1 is movement across columns.

Let's make an array and matrix to slice:


>>> A = arange(12)
>>> A
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> A.shape = (3,4)
>>> M = mat(A.copy())
>>> print type(A),"  ",type(M)
<type 'numpy.ndarray'>    <class 'numpy.core.defmatrix.matrix'>
>>> print A
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
>>> print M
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Now, let's take some simple slices. Basic slicing uses slice objects or integers. For example, the evaluation of A[:] and M[:] will appear familiar from Python indexing, however it is important to note that slicing NumPy arrays does *not* make a copy of the data; slicing provides a new view of the same data.


>>> print A[:]; print A[:].shape
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
(3, 4)
>>> print M[:]; print M[:].shape
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
(3, 4)
Now for something that differs from Python indexing: you may use comma-separated indices to index along multiple axes at the same time.


>>> print A[:,1]; print A[:,1].shape
[1 5 9]
(3,)
>>> print M[:,1]; print M[:,1].shape
[[1]
 [5]
 [9]]
(3, 1)
Notice the difference in the last two results. Use of a single colon for the 2D array produces a 1-dimensional array, while for a matrix it produces a 2-dimensional matrix. A slice of a matrix will always produce a matrix. For example, a slice M[2,:] produces a matrix of shape (1,4). In contrast, a slice of an array will always produce an array of the lowest possible dimension. For example, if C were a 3-dimensional array, C[...,1] produces a 2D array while C[1,:,1] produces a 1-dimensional array. From this point on, we will show results only for the array slice if the results for the corresponding matrix slice are identical.

Lets say that we wanted the 1st and 3rd column of an array. One way is to slice using a list:


>>> A[:,[1,3]]
array([[ 1,  3],
       [ 5,  7],
       [ 9, 11]])
A slightly more complicated way is to use the take() method:


>>> A[:,].take([1,3],axis=1)
array([[ 1,  3],
       [ 5,  7],
       [ 9, 11]])
If we wanted to skip the first row, we could use:


>>> A[1:,].take([1,3],axis=1)
array([[ 5,  7],
       [ 9, 11]])
Or we could simply use A[1:,[1,3]]. Yet another way to slice the above is to use a cross product:


>>> A[ix_((1,2),(1,3))]
array([[ 5,  7],
       [ 9, 11]])
For the reader's convenience, here is our array again:


>>> print A
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Now let's do something a bit more complicated. Lets say that we want to retain all columns where the first row is greater than 1. One way is to create a boolean index:


>>> A[0,:]>1
array([False, False, True, True], dtype=bool)
>>> A[:,A[0,:]>1]
array([[ 2,  3],
       [ 6,  7],
       [10, 11]])
Just what we wanted! But indexing the matrix is not so convenient.


>>> M[0,:]>1
matrix([[False, False, True, True]], dtype=bool)
>>> M[:,M[0,:]>1]
matrix([[2, 3]])
The problem of course is that slicing the matrix slice produced a matrix. But matrices have a convenient 'A' attribute whose value is the array representation, so we can just do this instead:


>>> M[:,M.A[0,:]>1]
matrix([[ 2,  3],
        [ 6,  7],
        [10, 11]])
If we wanted to conditionally slice the matrix in two directions, we must adjust our strategy slightly. Instead of


>>> A[A[:,0]>2,A[0,:]>1]
array([ 6, 11])
>>> M[M.A[:,0]>2,M.A[0,:]>1]
matrix([[ 6, 11]])
we need to use the cross product 'ix_':


>>> A[numpy.ix_(A[:,0]>2,A[0,:]>1)]
array([[ 6,  7],
       [10, 11]])
>>> M[numpy.ix_(M.A[:,0]>2,M.A[0,:]>1)]
matrix([[ 6,  7],
        [10, 11]])
Tricks and Tips

Here we give a list of short and useful tips.

"Automatic" Reshaping

To change the dimensions of an array, you can omit one of the sizes which will then be deduced automatically:


>>> a = arange(30)
>>> a.shape = 2,-1,3  # -1 means "whatever is needed"
>>> a.shape
(2, 5, 3)
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]],
       [[15, 16, 17],
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29]]])
Vector Stacking

How do we construct a 2D array from a list of equally-sized row vectors? In MATLAB this is quite easy: if x and y are two vectors of the same length you only need do m=[x;y]. In NumPy this works via the functions column_stack, dstack, hstack and vstack, depending on the dimension in which the stacking is to be done. For example:


x = arange(0,10,2)                     # x=([0,2,4,6,8])
y = arange(5)                          # y=([0,1,2,3,4])
m = vstack([x,y])                      # m=([[0,2,4,6,8],
                                       #     [0,1,2,3,4]])
xy = hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
The logic behind those functions in more than two dimensions can be strange.

See also NumPy_for_Matlab_Users and add your new findings there. ;-)

Histograms

The NumPy histogram function applied to an array returns a pair of vectors: the histogram of the array and the vector of bins. Beware: matplotlib also has a function to build histograms (called hist, as in Matlab) that differs from the one in NumPy. The main difference is that pylab.hist plots the histogram automatically, while numpy.histogram only generates the data.


import numpy
import pylab
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = numpy.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
pylab.show()
# Compute the histogram with numpy and then plot it
(n, bins) = numpy.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
pylab.plot(.5*(bins[1:]+bins[:-1]), n)
pylab.show()
References

The Python tutorial.
The Numpy_Example_List.
The nonexistent NumPy_Tutorial at scipy.org, where we can find the old Numeric documentation.
The Guide to NumPy book.
The SciPy_Tutorial and a SciPy course online
NumPy_for_Matlab_Users.
A matlab, R, IDL, NumPy/SciPy dictionary.
Attachments

This is an archival dump of old wiki content --- see scipy.org for current material
SciPy Numpy_Example_List
Attachments
This page contains a large database of examples demonstrating most of the Numpy functionality. Numpy_Example_List_With_Doc has these examples interleaved with the built-in documentation, but is not as regularly updated as this page. The examples here can be easily accessed from Python using the Numpy_Example_Fetcher.

This example list is incredibly useful, and we would like to get all the good examples and comments integrated in the official numpy documentation so that they are also shipped with numpy. You can help. The official numpy documentation can be edited on http://docs.scipy.org.


Contents
...
[]
abs()
absolute()
accumulate()
add()
all()
allclose()
alltrue()
angle()
any()
append()
apply_along_axis()
apply_over_axes()
arange()
arccos()
arccosh()
arcsin()
arcsinh()
arctan()
arctan2()
arctanh()
argmax()
argmin()
argsort()
array()
arrayrange()
array_split()
asarray()
asanyarray()
asmatrix()
astype()
atleast_1d()
atleast_2d()
atleast_3d()
average()
beta()
binary_repr()
bincount()
binomial()
bitwise_and()
bitwise_or()
bitwise_xor()
bmat()
broadcast()
bytes()
c_[]
cast[]()
ceil()
choose()
clip()
column_stack()
compress()
concatenate()
conj()
conjugate()
copy()
corrcoef()
cos()
cov()
cross()
cumprod()
cumsum()
delete()
det()
diag()
diagflat()
diagonal()
diff()
digitize()
dot()
dsplit()
dstack()
dtype()
empty()
empty_like()
expand_dims()
eye()
fft()
fftfreq()
fftshift()
fill()
finfo()
fix()
flat
flatten()
fliplr()
flipud()
floor()
fromarrays()
frombuffer()
fromfile()
fromfunction()
fromiter()
generic
gumbel()
histogram()
hsplit()
hstack()
hypot()
identity()
ifft()
imag
index_exp[]
indices()
inf
inner()
insert()
inv()
iscomplex()
iscomplexobj()
item()
ix_()
lexsort()
linspace()
loadtxt()
logical_and()
logical_not()
logical_or()
logical_xor()
logspace()
lstsq()
mat()
matrix()
max()
maximum()
mean()
median()
mgrid[]
min()
minimum()
multiply()
nan
ndenumerate()
ndim
ndindex()
newaxis
nonzero()
ogrid()
ones()
ones_like()
outer()
permutation()
piecewise()
pinv()
poisson()
poly1d()
polyfit()
prod()
ptp()
put()
putmask()
r_[]
rand()
randint()
randn()
random_integers()
random_sample()
ranf()
ravel()
real
recarray()
reduce()
repeat()
reshape()
resize()
rollaxis()
round()
rot90()
s_[]
sample()
savetxt()
searchsorted()
seed()
select()
set_printoptions()
shape
shuffle()
slice()
solve()
sometrue()
sort()
split()
squeeze()
std()
standard_normal()
sum()
svd()
swapaxes()
T
take()
tensordot()
tile()
tofile()
tolist()
trace()
transpose()
tri()
tril()
trim_zeros()
triu()
typeDict()
uniform()
unique()
unique1d()
vander()
var()
vdot()
vectorize()
view()
vonmises()
vsplit()
vstack()
weibull()
where()
zeros()
zeros_like()
 

...


>>> from numpy import *
>>> a = arange(12)
>>> a = a.reshape(3,2,2)
>>> print a
[[[ 0  1]
  [ 2  3]]
 [[ 4  5]
  [ 6  7]]
 [[ 8  9]
  [10 11]]]
>>> a[...,0]                               # same as a[:,:,0]
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10]])
>>> a[1:,...] # same as a[1:,:,:] or just a[1:]
array([[[ 4, 5],
        [ 6, 7]],
       [[ 8, 9],
        [10, 11]]])
See also: [], newaxis


[]


>>> from numpy import *
>>> a = array([ [ 0, 1, 2, 3, 4],
... [10,11,12,13,14],
... [20,21,22,23,24],
... [30,31,32,33,34] ])
>>>
>>> a[0,0] # indices start by zero
0
>>> a[-1] # last row
array([30, 31, 32, 33, 34])
>>> a[1:3,1:4] # subarray
array([[11, 12, 13],
       [21, 22, 23]])
>>>
>>> i = array([0,1,2,1]) # array of indices for the first axis
>>> j = array([1,2,3,4]) # array of indices for the second axis
>>> a[i,j]
array([ 1, 12, 23, 14])
>>>
>>> a[a<13] # boolean indexing
array([ 0, 1, 2, 3, 4, 10, 11, 12])
>>>
>>> b1 = array( [True,False,True,False] ) # boolean row selector
>>> a[b1,:]
array([[ 0, 1, 2, 3, 4],
       [20, 21, 22, 23, 24]])
>>>
>>> b2 = array( [False,True,True,False,True] ) # boolean column selector
>>> a[:,b2]
array([[ 1, 2, 4],
       [11, 12, 14],
       [21, 22, 24],
       [31, 32, 34]])
See also: ..., newaxis, ix_, indices, nonzero, where, slice


abs()


>>> from numpy import *
>>> abs(-1)
1
>>> abs(array([-1.2, 1.2]))
array([ 1.2, 1.2])
>>> abs(1.2+1j)
1.5620499351813308
See also: absolute, angle


absolute()

Synonym for abs()

See abs


accumulate()


>>> from numpy import *
>>> add.accumulate(array([1.,2.,3.,4.])) # like reduce() but also gives intermediate results
array([ 1., 3., 6., 10.])
>>> array([1., 1.+2., (1.+2.)+3., ((1.+2.)+3.)+4.]) # this is what it computed
array([ 1., 3., 6., 10.])
>>> multiply.accumulate(array([1.,2.,3.,4.])) # works also with other operands
array([ 1., 2., 6., 24.])
>>> array([1., 1.*2., (1.*2.)*3., ((1.*2.)*3.)*4.]) # this is what it computed
array([ 1., 2., 6., 24.])
>>> add.accumulate(array([[1,2,3],[4,5,6]]), axis = 0) # accumulate every column separately
array([[1, 2, 3],
       [5, 7, 9]])
>>> add.accumulate(array([[1,2,3],[4,5,6]]), axis = 1) # accumulate every row separately
array([[ 1, 3, 6],
       [ 4, 9, 15]])
See also: reduce, cumprod, cumsum


add()


>>> from numpy import *
>>> add(array([-1.2, 1.2]), array([1,3]))
array([-0.2, 4.2])
>>> array([-1.2, 1.2]) + array([1,3])
array([-0.2, 4.2])

all()


>>> from numpy import *
>>> a = array([True, False, True])
>>> a.all() # if all elements of a are True: return True; otherwise False
False
>>> all(a) # this form also exists
False
>>> a = array([1,2,3])
>>> all(a > 0) # equivalent to (a > 0).all()
True
See also: any, alltrue, sometrue


allclose()


>>> allclose(array([1e10,1e-7]), array([1.00001e10,1e-8]))
False
>>> allclose(array([1e10,1e-8]), array([1.00001e10,1e-9]))
True
>>> allclose(array([1e10,1e-8]), array([1.0001e10,1e-9]))
False

alltrue()


>>> from numpy import *
>>> b = array([True, False, True, True])
>>> alltrue(b)
False
>>> a = array([1, 5, 2, 7])
>>> alltrue(a >= 5)
False
See also: sometrue, all, any


angle()


>>> from numpy import *
>>> angle(1+1j) # in radians
0.78539816339744828
>>> angle(1+1j,deg=True) # in degrees
45.0
See also: real, imag, hypot


any()


>>> from numpy import *
>>> a = array([True, False, True])
>>> a.any() # gives True if at least 1 element of a is True, otherwise False
True
>>> any(a) # this form also exists
True
>>> a = array([1,2,3])
>>> (a >= 1).any() # equivalent to any(a >= 1)
True
See also: all, alltrue, sometrue


append()


>>> from numpy import *
>>> a = array([10,20,30,40])
>>> append(a,50)
array([10, 20, 30, 40, 50])
>>> append(a,[50,60])
array([10, 20, 30, 40, 50, 60])
>>> a = array([[10,20,30],[40,50,60],[70,80,90]])
>>> append(a,[[15,15,15]],axis=0)
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90],
       [15, 15, 15]])
>>> append(a,[[15],[15],[15]],axis=1)
array([[10, 20, 30, 15],
       [40, 50, 60, 15],
       [70, 80, 90, 15]])
See also: insert, delete, concatenate


apply_along_axis()


>>> from numpy import *
>>> def myfunc(a): # function works on a 1d arrays, takes the average of the 1st an last element
... return (a[0]+a[-1])/2
...
>>> b = array([[1,2,3],[4,5,6],[7,8,9]])
>>> apply_along_axis(myfunc,0,b) # apply myfunc to each column (axis=0) of b
array([4, 5, 6])
>>> apply_along_axis(myfunc,1,b) # apply myfunc to each row (axis=1) of b
array([2, 5, 8])
See also: apply_over_axes, vectorize


apply_over_axes()


>>> from numpy import *
>>> a = arange(24).reshape(2,3,4) # a has 3 axes: 0,1 and 2
>>> a
array([[[ 0, 1, 2, 3],
        [ 4, 5, 6, 7],
        [ 8, 9, 10, 11]],
       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
>>> apply_over_axes(sum, a, [0,2]) # sum over all axes except axis=1, result has same shape as original
array([[[ 60],
        [ 92],
        [124]]])
See also: apply_along_axis, vectorize


arange()


>>> from numpy import *
>>> arange(3)
array([0, 1, 2])
>>> arange(3.0)
array([ 0., 1., 2.])
>>> arange(3, dtype=float)
array([ 0., 1., 2.])
>>> arange(3,10) # start,stop
array([3, 4, 5, 6, 7, 8, 9])
>>> arange(3,10,2) # start,stop,step
array([3, 5, 7, 9])
See also: r_, linspace, logspace, mgrid, ogrid


arccos()


>>> from numpy import *
>>> arccos(array([0, 1]))
array([ 1.57079633, 0. ])
See also: arcsin, arccosh, arctan, arctan2


arccosh()


>>> from numpy import *
>>> arccosh(array([e, 10.0]))
array([ 1.65745445, 2.99322285])
See also: arccos, arcsinh, arctanh


arcsin()


>>> from numpy import *
>>> arcsin(array([0, 1]))
array([ 0. , 1.57079633])
See also: arccos, arctan, arcsinh


arcsinh()


>>> from numpy import *
>>> arcsinh(array([e, 10.0]))
array([ 1.72538256, 2.99822295])
See also: arccosh, arcsin, arctanh


arctan()


>>> from numpy import *
>>> arctan(array([0, 1]))
array([ 0. , 0.78539816])
See also: arccos, arcsin, arctanh


arctan2()


>>> from numpy import *
>>> arctan2(array([0, 1]), array([1, 0]))
array([ 0. , 1.57079633])
See also: arcsin, arccos, arctan, arctanh


arctanh()


>>> from numpy import *
>>> arctanh(array([0, -0.5]))
array([ 0. , -0.54930614])
See also: arcsinh, arccosh, arctan, arctan2


argmax()


>>> from numpy import *
>>> a = array([10,20,30])
>>> maxindex = a.argmax()
>>> a[maxindex]
30
>>> a = array([[10,50,30],[60,20,40]])
>>> maxindex = a.argmax()
>>> maxindex
3
>>> a.ravel()[maxindex]
60
>>> a.argmax(axis=0) # for each column: the row index of the maximum value
array([1, 0, 1])
>>> a.argmax(axis=1) # for each row: the column index of the maximum value
array([1, 0])
>>> argmax(a) # also exists, slower, default is axis=-1
array([1, 0])
See also: argmin, nan, min, max, maximum, minimum


argmin()


>>> from numpy import *
>>> a = array([10,20,30])
>>> minindex = a.argmin()
>>> a[minindex]
10
>>> a = array([[10,50,30],[60,20,40]])
>>> minindex = a.argmin()
>>> minindex
0
>>> a.ravel()[minindex]
10
>>> a.argmin(axis=0) # for each column: the row index of the minimum value
array([0, 1, 0])
>>> a.argmin(axis=1) # for each row: the column index of the minimum value
array([0, 1])
>>> argmin(a) # also exists, slower, default is axis=-1
array([0, 1])
See also: argmax, nan, min, max, maximum, minimum


argsort()

argsort(axis=-1, kind="quicksort")


>>> from numpy import *
>>> a = array([2,0,8,4,1])
>>> ind = a.argsort() # indices of sorted array using quicksort (default)
>>> ind
array([1, 4, 0, 3, 2])
>>> a[ind] # same effect as a.sort()
array([0, 1, 2, 4, 8])
>>> ind = a.argsort(kind='merge') # algorithm options are 'quicksort', 'mergesort' and 'heapsort'
>>> a = array([[8,4,1],[2,0,9]])
>>> ind = a.argsort(axis=0) # sorts on columns. NOT the same as a.sort(axis=1)
>>> ind
array([[1, 1, 0],
       [0, 0, 1]])
>>> a[ind,[[0,1,2],[0,1,2]]] # 2-D arrays need fancy indexing if you want to sort them.
array([[2, 0, 1],
       [8, 4, 9]])
>>> ind = a.argsort(axis=1) # sort along rows. Can use a.argsort(axis=-1) for last axis.
>>> ind
array([[2, 1, 0],
       [1, 0, 2]])
>>> a = ones(17)
>>> a.argsort() # quicksort doesn't preserve original order.
array([ 0, 14, 13, 12, 11, 10, 9, 15, 8, 6, 5, 4, 3, 2, 1, 7, 16])
>>> a.argsort(kind="mergesort") # mergesort preserves order when possible. It is a stable sort.
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
>>> ind = argsort(a) # there is a functional form
See also: lexsort, sort


array()


>>> from numpy import *
>>> array([1,2,3]) # conversion from a list to an array
array([1, 2, 3])
>>> array([1,2,3], dtype=complex) # output type is specified
array([ 1.+0.j, 2.+0.j, 3.+0.j])
>>> array(1, copy=0, subok=1, ndmin=1) # basically equivalent to atleast_1d
array([1])
>>> array(1, copy=0, subok=1, ndmin=2) # basically equivalent to atleast_2d
array([[1]])
>>> array(1, subok=1, ndmin=2) # like atleast_2d but always makes a copy
array([[1]])
>>> mydescriptor = {'names': ('gender','age','weight'), 'formats': ('S1', 'f4', 'f4')} # one way of specifying the data type
>>> a = array([('M',64.0,75.0),('F',25.0,60.0)], dtype=mydescriptor) # recarray
>>> print a
[('M', 64.0, 75.0) ('F', 25.0, 60.0)]
>>> a['weight']
array([ 75., 60.], dtype=float32)
>>> a.dtype.names # Access to the ordered field names
('gender','age','weight')
>>> mydescriptor = [('age',int16),('Nchildren',int8),('weight',float32)] # another way of specifying the data type
>>> a = array([(64,2,75.0),(25,0,60.0)], dtype=mydescriptor)
>>> a['Nchildren']
array([2, 0], dtype=int8)
>>> mydescriptor = dtype([('x', 'f4'),('y', 'f4'), # nested recarray
... ('nested', [('i', 'i2'),('j','i2')])])
>>> array([(1.0, 2.0, (1,2))], dtype=mydescriptor) # input one row
array([(1.0, 2.0, (1, 2))],
      dtype=[('x', '<f4'), ('y', '<f4'), ('nested', [('i', '<i2'), ('j', '<i2')])])
>>> array([(1.0, 2.0, (1,2)), (2.1, 3.2, (3,2))], dtype=mydescriptor) # input two rows
array([(1.0, 2.0, (1, 2)), (2.0999999046325684, 3.2000000476837158, (3, 2))],
      dtype=[('x', '<f4'), ('y', '<f4'), ('nested', [('i', '<i2'), ('j', '<i2')])])
>>> a=array([(1.0, 2.0, (1,2)), (2.1, 3.2, (3,2))], dtype=mydescriptor) # getting some columns
>>> a['x'] # a plain column
array([ 1. , 2.0999999], dtype=float32)
>>> a['nested'] # a nested column
array([(1, 2), (3, 2)],
      dtype=[('i', '<i2'), ('j', '<i2')])
>>> a['nested']['i'] # a plain column inside a nested column
>>> mydescriptor = dtype([('x', 'f4'),('y', 'f4'), # nested recarray
... ('nested', [('i', 'i2'),('j','i2')])])
>>> array([(1.0, 2.0, (1,2))], dtype=mydescriptor) # input one row
array([(1.0, 2.0, (1, 2))],
      dtype=[('x', '<f4'), ('y', '<f4'), ('nested', [('i', '<i2'), ('j', '<i2')])])
>>> array([(1.0, 2.0, (1,2)), (2.1, 3.2, (3,2))], dtype=mydescriptor) # input two rows
array([(1.0, 2.0, (1, 2)), (2.0999999046325684, 3.2000000476837158, (3, 2))],
      dtype=[('x', '<f4'), ('y', '<f4'), ('nested', [('i', '<i2'), ('j', '<i2')])])
>>> a=array([(1.0, 2.0, (1,2)), (2.1, 3.2, (3,2))], dtype=mydescriptor) # getting some columns
>>> a['x'] # a plain column
array([ 1. , 2.0999999], dtype=float32)
>>> a['nested'] # a nested column
array([(1, 2), (3, 2)],
      dtype=[('i', '<i2'), ('j', '<i2')])
>>> a['nested']['i'] # a plain column inside a nested column
array([1, 3], dtype=int16)
See also: dtype, mat, asarray


arrayrange()

Synonym for arange()

See arange


array_split()


>>> from numpy import *
>>> a = array([[1,2,3,4],[5,6,7,8]])
>>> array_split(a,2,axis=0) # split a in 2 parts. row-wise
[array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]
>>> array_split(a,4,axis=1) # split a in 4 parts, column-wise
[array([[1],
       [5]]), array([[2],
       [6]]), array([[3],
       [7]]), array([[4],
       [8]])]
 >>> array_split(a,3,axis=1) # impossible to split in 3 equal parts -> first part(s) are bigger
[array([[1, 2],
       [5, 6]]), array([[3],
       [7]]), array([[4],
       [8]])]
>>> array_split(a,[2,3],axis=1) # make a split before the 2nd and the 3rd column
[array([[1, 2],
       [5, 6]]), array([[3],
       [7]]), array([[4],
       [8]])]
See also: dsplit, hsplit, vsplit, split, concatenate


asarray()


>>> from numpy import *
>>> m = matrix('1 2; 5 8')
>>> m
matrix([[1, 2],
       [5, 8]])
>>> a = asarray(m) # a is array type with same contents as m -- data is not copied
>>> a
array([[1, 2],
       [5, 8]])
>>> m[0,0] = -99
>>> m
matrix([[-99, 2],
       [ 5, 8]])
>>> a # no copy was made, so modifying m modifies a, and vice versa
array([[-99, 2],
       [ 5, 8]])
See also: asmatrix, array, matrix, mat


asanyarray()


>>> from numpy import *
>>> a = array([[1,2],[5,8]])
>>> a
array([[1, 2],
       [5, 8]])
>>> m = matrix('1 2; 5 8')
>>> m
matrix([[1, 2],
       [5, 8]])
>>> asanyarray(a) # the array a is returned unmodified
array([[1, 2],
       [5, 8]])
>>> asanyarray(m) # the matrix m is returned unmodified
matrix([[1, 2],
       [5, 8]])
>>> asanyarray([1,2,3]) # a new array is constructed from the list
array([1, 2, 3])
See also: asmatrix, asarray, array, mat


asmatrix()


>>> from numpy import *
>>> a = array([[1,2],[5,8]])
>>> a
array([[1, 2],
       [5, 8]])
>>> m = asmatrix(a) # m is matrix type with same contents as a -- data is not copied
>>> m
matrix([[1, 2],
       [5, 8]])
>>> a[0,0] = -99
>>> a
array([[-99, 2],
       [ 5, 8]])
>>> m # no copy was made so modifying a modifies m, and vice versa
matrix([[-99, 2],
       [ 5, 8]])
See also: asarray, array, matrix, mat


astype()


>>> from numpy import *
>>> x = array([1,2,3])
>>> y = x.astype(float64) # convert from int32 to float64
>>> type(y[0])
<type 'numpy.float64'>
>>> x.astype(None) # None implies converting to the default (float64)
array([1., 2., 3.])
See also: cast, dtype, ceil, floor, round_, fix


atleast_1d()


>>> from numpy import *
>>> a = 1 # 0-d array
>>> b = array([2,3]) # 1-d array
>>> c = array([[4,5],[6,7]]) # 2-d array
>>> d = arange(8).reshape(2,2,2) # 3-d array
>>> d
array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])
>>> atleast_1d(a,b,c,d) # all output arrays have dim >= 1
[array([1]), array([2, 3]), array([[4, 5],
       [6, 7]]), array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])]
See also: atleast_2d, atleast_3d, newaxis, expand_dims


atleast_2d()


>>> from numpy import *
>>> a = 1 # 0-d array
>>> b = array([2,3]) # 1-d array
>>> c = array([[4,5],[6,7]]) # 2-d array
>>> d = arange(8).reshape(2,2,2) # 3-d array
>>> d
array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])
>>> atleast_2d(a,b,c,d) # all output arrays have dim >= 2
[array([[1]]), array([[2, 3]]), array([[4, 5],
       [6, 7]]), array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])]
See also: atleast_1d, atleast_3d, newaxis, expand_dims


atleast_3d()


>>> from numpy import *
>>> a = 1 # 0-d array
>>> b = array([2,3]) # 1-d array
>>> c = array([[4,5],[6,7]]) # 2-d array
>>> d = arange(8).reshape(2,2,2) # 3-d array
>>> d
array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])
>>> atleast_3d(a,b,c,d) # all output arrays have dim >= 3
[array([[[1]]]), array([[[2],
        [3]]]), array([[[4],
        [5]],
       [[6],
        [7]]]), array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])]
See also: atleast_1d, atleast_2d, newaxis, expand_dims


average()


>>> from numpy import *
>>> a = array([1,2,3,4,5])
>>> w = array([0.1, 0.2, 0.5, 0.2, 0.2]) # weights, not necessarily normalized
>>> average(a) # plain mean value
3.0
>>> average(a,weights=w) # weighted average
3.1666666666666665
>>> average(a,weights=w,returned=True) # output = weighted average, sum of weights
(3.1666666666666665, 1.2)
See also: mean, median


beta()


>>> from numpy import *
>>> from numpy.random import *
>>> beta(a=1,b=10,size=(2,2)) # Beta distribution alpha=1, beta=10
array([[ 0.02571091, 0.04973536],
       [ 0.04887027, 0.02382052]])
See also: seed


binary_repr()


>>> from numpy import *
>>> a = 25
>>> binary_repr(a) # binary representation of 25
'11001'
>>> b = float_(pi) # numpy float has extra functionality ...
>>> b.nbytes # ... like the number of bytes it takes
8
>>> binary_repr(b.view('u8')) # view float number as an 8 byte integer, then get binary bitstring
'1010100010001000010110100011000'

bincount()


>>> from numpy import *
>>> a = array([1,1,1,1,2,2,4,4,5,6,6,6]) # doesn't need to be sorted
>>> bincount(a) # 0 occurs 0 times, 1 occurs 4 times, 2 occurs twice, 3 occurs 0 times, ...
array([0, 4, 2, 0, 2, 1, 3])
>>> a = array([5,4,4,2,2])
>>> w = array([0.1, 0.2, 0.1, 0.3, 0.5])
>>> bincount(a) # 0 & 1 don't occur, 2 occurs twice, 3 doesn't occur, 4 occurs twice, 5 once
array([0, 0, 2, 0, 2, 1])
>>> bincount(a, weights=w)
array([ 0. , 0. , 0.8, 0. , 0.3, 0.1])
>>> # 0 occurs 0 times -> result[0] = 0
>>> # 1 occurs 0 times -> result[1] = 0
>>> # 2 occurs at indices 3 & 4 -> result[2] = w[3] + w[4]
>>> # 3 occurs 0 times -> result[3] = 0
>>> # 4 occurs at indices 1 & 2 -> result[4] = w[1] + w[2]
>>> # 5 occurs at index 0 -> result[5] = w[0]
See also: histogram, digitize


binomial()


>>> from numpy import *
>>> from numpy.random import *
>>> binomial(n=100,p=0.5,size=(2,3)) # binomial distribution n trials, p= success probability
array([[38, 50, 53],
       [56, 48, 54]])
>>> from pylab import * # histogram plot example
>>> hist(binomial(100,0.5,(1000)), 20)
See also: random_sample, uniform, standard_normal, seed


bitwise_and()


>>> from numpy import *
>>> bitwise_and(array([2,5,255]), array([4,4,4]))
array([0, 4, 4])
>>> bitwise_and(array([2,5,255,2147483647L],dtype=int32), array([4,4,4,2147483647L],dtype=int32))
array([ 0, 4, 4, 2147483647])
See also: bitwise_or, bitwise_xor, logical_and


bitwise_or()


>>> from numpy import *
>>> bitwise_or(array([2,5,255]), array([4,4,4]))
array([ 6, 5, 255])
>>> bitwise_or(array([2,5,255,2147483647L],dtype=int32), array([4,4,4,2147483647L],dtype=int32))
array([ 6, 5, 255, 2147483647])
See also: bitwise_and, bitwise_xor, logical_or


bitwise_xor()


>>> from numpy import *
>>> bitwise_xor(array([2,5,255]), array([4,4,4]))
array([ 6, 1, 251])
>>> bitwise_xor(array([2,5,255,2147483647L],dtype=int32), array([4,4,4,2147483647L],dtype=int32))
array([ 6, 1, 251, 0])
See also: bitwise_and, bitwise_or, logical_xor


bmat()


>>> from numpy import *
>>> a = mat('1 2; 3 4')
>>> b = mat('5 6; 7 8')
>>> bmat('a b; b a') # all elements must be existing symbols
matrix([[1, 2, 5, 6],
       [3, 4, 7, 8],
       [5, 6, 1, 2],
       [7, 8, 3, 4]])
See also: mat


broadcast()


>>> from numpy import *
>>> a = array([[1,2],[3,4]])
>>> b = array([5,6])
>>> c = broadcast(a,b)
>>> c.nd # the number of dimensions in the broadcasted result
2
>>> c.shape # the shape of the broadcasted result
(2, 2)
>>> c.size # total size of the broadcasted result
4
>>> for value in c: print value
...
(1, 5)
(2, 6)
(3, 5)
(4, 6)
>>> c.reset() # reset the iterator to the beginning
>>> c.next() # next element
(1, 5)
See also: ndenumerate, ndindex, flat


bytes()


>>> from numpy import *
>>> from numpy.random import bytes
>>> print repr(bytes(5)) # string of 5 random bytes
'o\x07\x9f\xdf\xdf'
>>> print repr(bytes(5)) # another string of 5 random bytes
'\x98\xc9KD\xe0'
See also: shuffle, permutation, seed


c_[]


>>> from numpy import *
>>> c_[1:5] # for single ranges, c_ works like r_
array([1, 2, 3, 4])
>>> c_[1:5,2:6] # for comma separated values, c_ stacks column-wise
array([[1, 2],
       [2, 3],
       [3, 4],
       [4, 5]])
>>> a = array([[1,2,3],[4,5,6]])
>>> c_[a,a] # concatenation along last (default) axis (column-wise, that's why it's called c_)
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])
>>> c_['0',a,a] # concatenation along 1st axis, equivalent to r_[a,a]
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
See also: r_, hstack, vstack, column_stack, concatenate, bmat, s_


cast[]()


>>> from numpy import *
>>> x = arange(3)
>>> x.dtype
dtype('int32')
>>> cast['int64'](x)
array([0, 1, 2], dtype=int64)
>>> cast['uint'](x)
array([0, 1, 2], dtype=uint32)
>>> cast[float128](x)
array([0.0, 1.0, 2.0], dtype=float128)
>>> cast.keys() # list dtype cast possibilities
<snip>
See also: astype, typeDict


ceil()


>>> from numpy import *
>>> a = array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7])
>>> ceil(a) # nearest integers greater-than or equal to a
array([-1., -1., -0., 1., 2., 2.])
See also: floor, round_, fix, astype


choose()


>>> from numpy import *
>>> choice0 =array([10,12,14,16]) # selector and choice arrays must be equally sized
>>> choice1 =array([20,22,24,26])
>>> choice2 =array([30,32,34,36])
>>> selector = array([0,0,2,1]) # selector can only contain integers in range(number_of_choice_arrays)
>>> selector.choose(choice0,choice1,choice2)
array([10, 12, 34, 26])
>>> a = arange(4)
>>> choose(a >= 2, (choice0, choice1)) # separate function also exists
array([10, 12, 24, 26])
See also: compress, take, where, select


clip()


>>> from numpy import *
>>> a = array([5,15,25,3,13])
>>> a.clip(min=10,max=20)
array([10, 15, 20, 10, 13])
>>> clip(a,10,20) # this syntax also exists
See also: where compress


column_stack()


>>> from numpy import *
>>> a = array([1,2])
>>> b = array([3,4])
>>> c = array([5,6])
>>> column_stack((a,b,c)) # a,b,c are 1-d arrays with equal length
array([[1, 3, 5],
       [2, 4, 6]])
See also: concatenate, dstack, hstack, vstack, c_


compress()


>>> from numpy import *
>>> a = array([10, 20, 30, 40])
>>> condition = (a > 15) & (a < 35)
>>> condition
array([False, True, True, False], dtype=bool)
>>> a.compress(condition)
array([20, 30])
>>> a[condition] # same effect
array([20, 30])
>>> compress(a >= 30, a) # this form also exists
array([30, 40])
>>> b = array([[10,20,30],[40,50,60]])
>>> b.compress(b.ravel() >= 22)
array([30, 40, 50, 60])
>>> x = array([3,1,2])
>>> y = array([50, 101])
>>> b.compress(x >= 2, axis=1) # illustrates the use of the axis keyword
array([[10, 30],
       [40, 60]])
>>> b.compress(y >= 100, axis=0)
array([[40, 50, 60]])
See also: choose, take, where, trim_zeros, unique, unique1d


concatenate()


>>> from numpy import *
>>> x = array([[1,2],[3,4]])
>>> y = array([[5,6],[7,8]])
>>> concatenate((x,y)) # default is axis=0
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
>>> concatenate((x,y),axis=1)
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
See also: append, column_stack, dstack, hstack, vstack, array_split


conj()

Synonym for conjugate()

See conjugate()


conjugate()


>>> a = array([1+2j,3-4j])
>>> a.conj() # .conj() and .conjugate() are the same
array([ 1.-2.j, 3.+4.j])
>>> a.conjugate()
array([ 1.-2.j, 3.+4.j])
>>> conj(a) # is also possible
>>> conjugate(a) # is also possible
See also: vdot


copy()


>>> from numpy import *
>>> a = array([1,2,3])
>>> a
array([1, 2, 3])
>>> b = a # b is a reference to a
>>> b[1] = 4
>>> a
array([1, 4, 3])
>>> a = array([1,2,3])
>>> b = a.copy() # b is now an independent copy of a
>>> b[1] = 4
>>> a
array([1, 2, 3])
>>> b
array([1, 4, 3])
See also: view


corrcoef()


>>> from numpy import *
>>> T = array([1.3, 4.5, 2.8, 3.9]) # temperature measurements
>>> P = array([2.7, 8.7, 4.7, 8.2]) # corresponding pressure measurements
>>> print corrcoef([T,P]) # correlation matrix of temperature and pressure
[[ 1. 0.98062258]
 [ 0.98062258 1. ]]
>>> rho = array([8.5, 5.2, 6.9, 6.5]) # corresponding density measurements
>>> data = column_stack([T,P,rho])
>>> print corrcoef([T,P,rho]) # correlation matrix of T,P and rho
[[ 1. 0.98062258 -0.97090288]
 [ 0.98062258 1. -0.91538464]
 [-0.97090288 -0.91538464 1. ]]
See also: cov, var


cos()


>>> cos(array([0, pi/2, pi]))
array([ 1.00000000e+00, 6.12303177e-17, -1.00000000e+00])

cov()


>>> from numpy import *
>>> x = array([1., 3., 8., 9.])
>>> variance = cov(x) # normalized by N-1
>>> variance = cov(x, bias=1) # normalized by N
>>> T = array([1.3, 4.5, 2.8, 3.9]) # temperature measurements
>>> P = array([2.7, 8.7, 4.7, 8.2]) # corresponding pressure measurements
>>> cov(T,P) # covariance between temperature and pressure
3.9541666666666657
>>> rho = array([8.5, 5.2, 6.9, 6.5]) # corresponding density measurements
>>> data = column_stack([T,P,rho])
>>> print cov(data) # covariance matrix of T,P and rho
[[ 1.97583333 3.95416667 -1.85583333]
 [ 3.95416667 8.22916667 -3.57083333]
 [-1.85583333 -3.57083333 1.84916667]]
See also: corrcoef, std, var


cross()


>>> from numpy import *
>>> x = array([1,2,3])
>>> y = array([4,5,6])
>>> cross(x,y) # vector cross-product
array([-3, 6, -3])
See also: inner, ix_, outer


cumprod()


>>> from numpy import *
>>> a = array([1,2,3])
>>> a.cumprod() # total product 1*2*3 = 6, and intermediate results 1, 1*2
array([1, 2, 6])
>>> cumprod(a) # also exists
array([1, 2, 6])
>>> a = array([[1,2,3],[4,5,6]])
>>> a.cumprod(dtype=float) # specify type of output
array([1., 2., 6., 24., 120., 720.])
>>> a.cumprod(axis=0) # for each of the 3 columns: product and intermediate results
array([[ 1, 2, 3],
       [ 4, 10, 18]])
>>> a.cumprod(axis=1) # for each of the two rows: product and intermediate results
array([[ 1, 2, 6],
       [ 4, 20, 120]])
See also: accumulate, prod, cumsum


cumsum()


>>> from numpy import *
>>> a = array([1,2,3]) # cumulative sum = intermediate summing results & total sum
>>> a.cumsum()
array([1, 3, 6])
>>> cumsum(a) # also exists
array([1, 3, 6])
>>> a = array([[1,2,3],[4,5,6]])
>>> a.cumsum(dtype=float) # specifies type of output value(s)
array([ 1., 3., 6., 10., 15., 21.])
>>> a.cumsum(axis=0) # sum over rows for each of the 3 columns
array([[1, 2, 3],
       [5, 7, 9]])
>>> a.cumsum(axis=1) # sum over columns for each of the 2 rows
array([[ 1, 3, 6],
       [ 4, 9, 15]])
See also: accumulate, sum, cumprod


delete()


>>> from numpy import *
>>> a = array([0, 10, 20, 30, 40])
>>> delete(a, [2,4]) # remove a[2] and a[4]
array([ 0, 10, 30])
>>> a = arange(16).reshape(4,4)
>>> a
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11],
       [12, 13, 14, 15]])
>>> delete(a, s_[1:3], axis=0) # remove rows 1 and 2
array([[ 0, 1, 2, 3],
       [12, 13, 14, 15]])
>>> delete(a, s_[1:3], axis=1) # remove columns 1 and 2
array([[ 0, 3],
       [ 4, 7],
       [ 8, 11],
       [12, 15]])
See also: append, insert


det()


>>> from numpy import *
>>> from numpy.linalg import det
>>> A = array([[1., 2.],[3., 4.]])
>>> det(A) # determinant of square matrix
-2.0
See also: inv


diag()


>>> from numpy import *
>>> a = arange(12).reshape(4,3)
>>> print a
[[ 0 1 2]
 [ 3 4 5]
 [ 6 7 8]
 [ 9 10 11]]
>>> print diag(a,k=0)
[0 4 8]
>>> print diag(a,k=1)
[1 5]
>>> print diag(array([1,4,5]),k=0)
[[1 0 0]
 [0 4 0]
 [0 0 5]]
>>> print diag(array([1,4,5]),k=1)
[[0 1 0 0]
 [0 0 4 0]
 [0 0 0 5]
 [0 0 0 0]]
See also: diagonal, diagflat, trace


diagflat()


>>> from numpy import *
>>> x = array([[5,6],[7,8]])
>>> diagflat(x) # flatten x, then put elements on diagonal
array([[5, 0, 0, 0],
       [0, 6, 0, 0],
       [0, 0, 7, 0],
       [0, 0, 0, 8]])
See also: diag, diagonal, flatten


diagonal()


>>> from numpy import *
>>> a = arange(12).reshape(3,4)
>>> print a
[[ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]]
>>> a.diagonal()
array([ 0, 5, 10])
>>> a.diagonal(offset=1)
array([ 1, 6, 11])
>>> diagonal(a) # Also this form exists
array([ 0, 5, 10])
See also: diag, diagflat, trace


diff()


>>> from numpy import *
>>> x = array([0,1,3,9,5,10])
>>> diff(x) # 1st-order differences between the elements of x
array([ 1, 2, 6, -4, 5])
>>> diff(x,n=2) # 2nd-order differences, equivalent to diff(diff(x))
array([ 1, 4, -10, 9])
>>> x = array([[1,3,6,10],[0,5,6,8]])
>>> diff(x) # 1st-order differences between the columns (default: axis=-1)
array([[2, 3, 4],
       [5, 1, 2]])
>>> diff(x,axis=0) # 1st-order difference between the rows
array([[-1, 2, 0, -2]])

digitize()


>>> from numpy import *
>>> x = array([0.2, 6.4, 3.0, 1.6])
>>> bins = array([0.0, 1.0, 2.5, 4.0, 10.0]) # monotonically increasing
>>> d = digitize(x,bins) # in which bin falls each value of x?
>>> d
array([1, 4, 3, 2])
>>> for n in range(len(x)):
... print bins[d[n]-1], "<=", x[n], "<", bins[d[n]]
...
0.0 <= 0.2 < 1.0
4.0 <= 6.4 < 10.0
2.5 <= 3.0 < 4.0
1.0 <= 1.6 < 2.5
See also: bincount, histogram


dot()


>>> from numpy import *
>>> x = array([[1,2,3],[4,5,6]])
>>> x.shape
(2, 3)
>>> y = array([[1,2],[3,4],[5,6]])
>>> y.shape
(3, 2)
>>> dot(x,y) # matrix multiplication (2,3) x (3,2) -> (2,2)
array([[22, 28],
       [49, 64]])
>>>
>>> import numpy
>>> if id(dot) == id(numpy.core.multiarray.dot): # A way to know if you use fast blas/lapack or not.
... print "Not using blas/lapack!"
See also: vdot, inner, multiply


dsplit()


>>> from numpy import *
>>> a = array([[1,2],[3,4]])
>>> b = dstack((a,a,a,a))
>>> b.shape # stacking in depth: for k in (0,..,3): b[:,:,k] = a
(2, 2, 4)
>>> c = dsplit(b,2) # split, depth-wise, in 2 equal parts
>>> print c[0].shape, c[1].shape # for k in (0,1): c[0][:,:,k] = a and c[1][:,:,k] = a
(2, 2, 2) (2, 2, 2)
>>> d = dsplit(b,[1,2]) # split before [:,:,1] and before [:,:,2]
>>> print d[0].shape, d[1].shape, d[2].shape # for any of the parts: d[.][:,:,k] = a
(2, 2, 1) (2, 2, 1) (2, 2, 2)
See also: split, array_split, hsplit, vsplit, dstack


dstack()


>>> from numpy import *
>>> a = array([[1,2],[3,4]]) # shapes of a and b can only differ in the 3rd dimension (if present)
>>> b = array([[5,6],[7,8]])
>>> dstack((a,b)) # stack arrays along a third axis (depth wise)
array([[[1, 5],
        [2, 6]],
       [[3, 7],
        [4, 8]]])
See also: column_stack, concatenate, hstack, vstack, dsplit


dtype()


>>> from numpy import *
>>> dtype('int16') # using array-scalar type
dtype('int16')
>>> dtype([('f1', 'int16')]) # record, 1 field named 'f1', containing int16
dtype([('f1', '<i2')])
>>> dtype([('f1', [('f1', 'int16')])]) # record, 1 field named 'f1' containing a record that has 1 field.
dtype([('f1', [('f1', '<i2')])])
>>> dtype([('f1', 'uint'), ('f2', 'int32')]) # record with 2 fields: field 1 contains an unsigned int, 2nd field an int32
dtype([('f1', '<u4'), ('f2', '<i4')])
>>> dtype([('a','f8'),('b','S10')]) # using array-protocol type strings
dtype([('a', '<f8'), ('b', '|S10')])
>>> dtype("i4, (2,3)f8") # using comma-separated field formats. (2,3) is the shape
dtype([('f0', '<i4'), ('f1', '<f8', (2, 3))])
>>> dtype([('hello',('int',3)),('world','void',10)]) # using tuples. int is fixed-type: 3 is shape; void is flex-type: 10 is size.
dtype([('hello', '<i4', 3), ('world', '|V10')])
>>> dtype(('int16', {'x':('int8',0), 'y':('int8',1)})) # subdivide int16 in 2 int8, called x and y. 0 and 1 are the offsets in bytes
dtype(('<i2', [('x', '|i1'), ('y', '|i1')]))
>>> dtype({'names':['gender','age'], 'formats':['S1',uint8]}) # using dictionaries. 2 fields named 'gender' and 'age'
dtype([('gender', '|S1'), ('age', '|u1')])
>>> dtype({'surname':('S25',0),'age':(uint8,25)}) # 0 and 25 are offsets in bytes
dtype([('surname', '|S25'), ('age', '|u1')])
>>>
>>> a = dtype('int32')
>>> a
dtype('int32')
>>> a.type # type object
<type 'numpy.int32'>
>>> a.kind # character code (one of 'biufcSUV') to identify general type
'i'
>>> a.char # unique char code of each of the 21 built-in types
'l'
>>> a.num # unique number of each of the 21 built-in types
7
>>> a.str # array-protocol typestring
'<i4'
>>> a.name # name of this datatype
'int32'
>>> a.byteorder # '=':native, '<':little endian, '>':big endian, '|':not applicable
'='
>>> a.itemsize # item size in bytes
4
>>> a = dtype({'surname':('S25',0),'age':(uint8,25)})
>>> a.fields.keys()
['age', 'surname']
>>> a.fields.values()
[(dtype('uint8'), 25), (dtype('|S25'), 0)]
>>> a = dtype([('x', 'f4'),('y', 'f4'), # nested field
... ('nested', [('i', 'i2'),('j','i2')])])
>>> a.fields['nested'] # access nested fields
(dtype([('i', '<i2'), ('j', '<i2')]), 8)
>>> a.fields['nested'][0].fields['i'] # access nested fields
(dtype('int16'), 0)
>>> a.fields['nested'][0].fields['i'][0].type
<type 'numpy.int16'>
See also: array, typeDict, astype


empty()


>>> from numpy import *
>>> empty(3) # uninitialized array, size=3, dtype = float
array([ 6.08581638e+000, 3.45845952e-323, 4.94065646e-324])
>>> empty((2,3),int) # uninitialized array, dtype = int
array([[1075337192, 1075337192, 135609024],
       [1084062604, 1197436517, 1129066306]])
See also: ones, zeros, eye, identity


empty_like()


>>> from numpy import *
>>> a = array([[1,2,3],[4,5,6]])
>>> empty_like(a) # uninitialized array with the same shape and datatype as 'a'
array([[ 0, 25362433, 6571520],
       [ 21248, 136447968, 4]])
See also: ones_like, zeros_like


expand_dims()


>>> from numpy import *
>>> x = array([1,2])
>>> expand_dims(x,axis=0) # Equivalent to x[newaxis,:] or x[None] or x[newaxis]
array([[1, 2]])
>>> expand_dims(x,axis=1) # Equivalent to x[:,newaxis]
array([[1],
       [2]])
See also: newaxis, atleast_1d, atleast_2d, atleast_3d


eye()


>>> from numpy import *
>>> eye(3,4,0,dtype=float) # a 3x4 matrix containing zeros except for the 0th diagonal that contains ones
array([[ 1., 0., 0., 0.],
       [ 0., 1., 0., 0.],
       [ 0., 0., 1., 0.]])
>>> eye(3,4,1,dtype=float) # a 3x4 matrix containing zeros except for the 1st diagonal that contains ones
array([[ 0., 1., 0., 0.],
       [ 0., 0., 1., 0.],
       [ 0., 0., 0., 1.]])
See also: ones, zeros, empty, identity


fft()


>>> from numpy import *
>>> from numpy.fft import *
>>> signal = array([-2., 8., -6., 4., 1., 0., 3., 5.]) # could also be complex
>>> fourier = fft(signal)
>>> fourier
array([ 13. +0.j , 3.36396103 +4.05025253j,
         2. +1.j , -9.36396103-13.94974747j,
       -21. +0.j , -9.36396103+13.94974747j,
         2. -1.j , 3.36396103 -4.05025253j])
>>>
>>> N = len(signal)
>>> fourier = empty(N,complex)
>>> for k in range(N): # equivalent but much slower
... fourier[k] = sum(signal * exp(-1j*2*pi*k*arange(N)/N))
...
>>> timestep = 0.1 # if unit=day -> freq unit=cycles/day
>>> fftfreq(N, d=timestep) # freqs corresponding to 'fourier'
array([ 0. , 1.25, 2.5 , 3.75, -5. , -3.75, -2.5 , -1.25])
See also: ifft, fftfreq, fftshift


fftfreq()


>>> from numpy import *
>>> from numpy.fft import *
>>> signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])
>>> fourier = fft(signal)
>>> N = len(signal)
>>> timestep = 0.1 # if unit=day -> freq unit=cycles/day
>>> freq = fftfreq(N, d=timestep) # freqs corresponding to 'fourier'
>>> freq
array([ 0. , 1.25, 2.5 , 3.75, -5. , -3.75, -2.5 , -1.25])
>>>
>>> fftshift(freq) # freqs in ascending order
array([-5. , -3.75, -2.5 , -1.25, 0. , 1.25, 2.5 , 3.75])
See also: fft, ifft, fftshift


fftshift()


>>> from numpy import *
>>> from numpy.fft import *
>>> signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])
>>> fourier = fft(signal)
>>> N = len(signal)
>>> timestep = 0.1 # if unit=day -> freq unit=cycles/day
>>> freq = fftfreq(N, d=timestep) # freqs corresponding to 'fourier'
>>> freq
array([ 0. , 1.25, 2.5 , 3.75, -5. , -3.75, -2.5 , -1.25])
>>>
>>> freq = fftshift(freq) # freqs in ascending order
>>> freq
array([-5. , -3.75, -2.5 , -1.25, 0. , 1.25, 2.5 , 3.75])
>>> fourier = fftshift(fourier) # adjust fourier to new freq order
>>>
>>> freq = ifftshift(freq) # undo previous frequency shift
>>> fourier = ifftshift(fourier) # undo previous fourier shift
See also: fft, ifft, fftfreq


fill()


>>> from numpy import *
>>> a = arange(4, dtype=int)
>>> a
array([0, 1, 2, 3])
>>> a.fill(7) # replace all elements with the number 7
>>> a
array([7, 7, 7, 7])
>>> a.fill(6.5) # fill value is converted to dtype of a
>>> a
array([6, 6, 6, 6])
See also: empty, zeros, ones, repeat


finfo()


>>> from numpy import *
>>> f = finfo(float) # the numbers given are machine dependent
>>> f.nmant, f.nexp # nr of bits in the mantissa and in the exponent
(52, 11)
>>> f.machep # most negative n so that 1.0 + 2**n != 1.0
-52
>>> f.eps # floating point precision: 2**machep
array(2.2204460492503131e-16)
>>> f.precision # nr of precise decimal digits: int(-log10(eps))
15
>>> f.resolution # 10**(-precision)
array(1.0000000000000001e-15)
>>> f.negep # most negative n so that 1.0 - 2**n != 1.0
-53
>>> f.epsneg # floating point precision: 2**negep
array(1.1102230246251565e-16)
>>> f.minexp # most negative n so that 2**n gives normal numbers
-1022
>>> f.tiny # smallest usuable floating point nr: 2**minexp
array(2.2250738585072014e-308)
>>> f.maxexp # smallest positive n so that 2**n causes overflow
1024
>>> f.min, f.max # the most negative and most positive usuable floating number
(-1.7976931348623157e+308, array(1.7976931348623157e+308))

fix()


>>> from numpy import *
>>> a = array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7])
>>> fix(a) # round a to nearest integer towards zero
array([-1., -1., 0., 0., 1., 1.])
See also: round_, ceil, floor, astype


flat


>>> from numpy import *
>>> a = array([[10,30],[40,60]])
>>> iter = a.flat # .flat returns an iterator
>>> iter.next() # cycle through array with .next()
10
>>> iter.next()
30
>>> iter.next()
40
See also: broadcast, flatten


flatten()


>>> from numpy import *
>>> a = array([[[1,2]],[[3,4]]])
>>> print a
[[[1 2]]
 [[3 4]]]
>>> b = a.flatten() # b is now a 1-d version of a, a new array, not a reference
>>> print b
[1 2 3 4]
See also: ravel, flat


fliplr()


>>> from numpy import *
>>> a = arange(12).reshape(4,3)
>>> a
array([[ 0, 1, 2],
       [ 3, 4, 5],
       [ 6, 7, 8],
       [ 9, 10, 11]])
>>> fliplr(a) # flip left-right
array([[ 2, 1, 0],
       [ 5, 4, 3],
       [ 8, 7, 6],
       [11, 10, 9]])
See also: flipud, rot90


flipud()


>>> from numpy import *
>>> a = arange(12).reshape(4,3)
>>> a
array([[ 0, 1, 2],
       [ 3, 4, 5],
       [ 6, 7, 8],
       [ 9, 10, 11]])
>>> flipud(a) # flip up-down
array([[ 9, 10, 11],
       [ 6, 7, 8],
       [ 3, 4, 5],
       [ 0, 1, 2]])
See also: fliplr, rot90


floor()


>>> from numpy import *
>>> a = array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7])
>>> floor(a)
array([-2., -2., -1., 0., 1., 1.]) # nearest integer smaller-than or equal to a # nearest integers greater-than or equal to a
See also: ceil, round_, fix, astype


fromarrays()


>>> from numpy import *
>>> x = array(['Smith','Johnson','McDonald']) # datatype is string
>>> y = array(['F','F','M'], dtype='S1') # datatype is a single character
>>> z = array([20,25,23]) # datatype is integer
>>> data = rec.fromarrays([x,y,z], names='surname, gender, age') # convert to record array
>>> data[0]
('Smith', 'F', 20)
>>> data.age # names are available as attributes
array([20, 25, 23])
See also: view


frombuffer()


>>> from numpy import *
>>> buffer = "\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08\
... @\x00\x00\x00\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x14@\x00\x00\x00\x00\x00\x00\x18@"
>>> a = frombuffer(buffer, complex128)
>>> a
array([ 1.+2.j, 3.+4.j, 5.+6.j])
See also: fromfunction, fromfile


fromfile()


>>> from numpy import *
>>> y = array([2.,4.,6.,8.])
>>> y.tofile("myfile.dat") # binary format
>>> y.tofile("myfile.txt", sep='\n', format = "%e") # ascii format, one column, exponential notation
>>> fromfile('myfile.dat', dtype=float)
array([ 2., 4., 6., 8.])
>>> fromfile('myfile.txt', dtype=float, sep='\n')
array([ 2., 4., 6., 8.])
See also: loadtxt, fromfunction, tofile, frombuffer, savetxt


fromfunction()


>>> from numpy import *
>>> def f(i,j):
... return i**2 + j**2
...
>>> fromfunction(f, (3,3)) # evaluate functiom for all combinations of indices [0,1,2]x[0,1,2]
array([[0, 1, 4],
       [1, 2, 5],
       [4, 5, 8]])
See also: fromfile, frombuffer


fromiter()


>>> from numpy import *
>>> import itertools
>>> mydata = [[55.5, 40],[60.5, 70]] # List of lists
>>> mydescriptor = {'names': ('weight','age'), 'formats': (float32, int32)} # Descriptor of the data
>>> myiterator = itertools.imap(tuple,mydata) # Clever way of putting list of lists into iterator
                                                                                  # of tuples. E.g.: myiterator.next() == (55.5, 40.)
>>> a = fromiter(myiterator, dtype = mydescriptor)
>>> a
array([(55.5, 40), (60.5, 70)],
      dtype=[('weight', '<f4'), ('age', '<i4')])
See also: fromarrays, frombuffer, fromfile, fromfunction


generic


>>> from numpy import *
>>> numpyscalar = string_('7') # Convert to numpy scalar
>>> numpyscalar # Looks like a build-in scalar...
'7'
>>> type(numpyscalar) # ... but it isn't
<type 'numpy.string_'>
>>> buildinscalar = '7' # Build-in python scalar
>>> type(buildinscalar)
<type 'str'>
>>> isinstance(numpyscalar, generic) # Check if scalar is a NumPy one
True
>>> isinstance(buildinscalar, generic) # Example on how to recognize NumPy scalars
False

gumbel()


>>> from numpy import *
>>> from numpy.random import *
>>> gumbel(loc=0.0,scale=1.0,size=(2,3)) # Gumbel distribution location=0.0, scale=1.0
array([[-1.25923601, 1.68758144, 1.76620507],
       [ 1.96820048, -0.21219499, 1.83579566]])
>>> from pylab import * # histogram plot example
>>> hist(gumbel(0,1,(1000)), 50)
See also: random_sample, uniform, poisson, seed


histogram()


>>> from numpy import *
>>> x = array([0.2, 6.4, 3.0, 1.6, 0.9, 2.3, 1.6, 5.7, 8.5, 4.0, 12.8])
>>> bins = array([0.0, 1.0, 2.5, 4.0, 10.0]) # increasing monotonically
>>> N,bins = histogram(x,bins)
>>> N,bins
(array([2, 3, 1, 4]), array([ 0. , 1. , 2.5, 4. , 10. ]))
>>> for n in range(len(bins)-1):
... print "# ", N[n], "number fall into bin [", bins[n], ",", bins[n+1], "["
...
# 2 numbers fall into bin [ 0.0 , 1.0 [
# 3 numbers fall into bin [ 1.0 , 2.5 [
# 1 numbers fall into bin [ 2.5 , 4.0 [
# 4 numbers fall into bin [ 4.0 , 10.0 [
#
>>> N,bins = histogram(x,5,range=(0.0, 10.0)) # 5 bin boundaries in the range (0,10)
>>> N,bins
(array([4, 2, 2, 1, 2]), array([ 0., 2., 4., 6., 8.]))
>>> N,bins = histogram(x,5,range=(0.0, 10.0), normed=True) # normalize histogram, i.e. divide by len(x)
>>> N,bins
(array([ 0.18181818, 0.09090909, 0.09090909, 0.04545455, 0.09090909]), array([ 0., 2., 4., 6., 8.]))
See also: bincount, digitize


hsplit()


>>> from numpy import *
>>> a = array([[1,2,3,4],[5,6,7,8]])
>>> hsplit(a,2) # split, column-wise, in 2 equal parts
[array([[1, 2],
       [5, 6]]), array([[3, 4],
       [7, 8]])]
>>> hsplit(a,[1,2]) # split before column 1 and before column 2
[array([[1],
       [5]]), array([[2],
       [6]]), array([[3, 4],
       [7, 8]])]
See also: split, array_split, dsplit, vsplit, hstack


hstack()


>>> from numpy import *
>>> a =array([[1],[2]]) # 2x1 array
>>> b = array([[3,4],[5,6]]) # 2x2 array
>>> hstack((a,b,a)) # only the 2nd dimension of the arrays is allowed to be different
array([[1, 3, 4, 1],
       [2, 5, 6, 2]])
See also: column_stack, concatenate, dstack, vstack, hsplit


hypot()


>>> from numpy import *
>>> hypot(3.,4.) # hypotenuse: sqrt(3**2 + 4**2) = 5
5.0
>>> z = array([2+3j, 3+4j])
>>> hypot(z.real, z.imag) # norm of complex numbers
array([ 3.60555128, 5. ])
See also: angle, abs


identity()


>>> from numpy import *
>>> identity(3,float)
array([[ 1., 0., 0.],
       [ 0., 1., 0.],
       [ 0., 0., 1.]])
See also: empty, eye, ones, zeros


ifft()


>>> from numpy import *
>>> from numpy.fft import *
>>> signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])
>>> fourier = fft(signal)
>>> ifft(fourier) # Inverse fourier transform
array([-2. +0.00000000e+00j, 8. +1.51410866e-15j, -6. +3.77475828e-15j,
        4. +2.06737026e-16j, 1. +0.00000000e+00j, 0. -1.92758271e-15j,
        3. -3.77475828e-15j, 5. +2.06737026e-16j])
>>>
>>> allclose(signal.astype(complex), ifft(fft(signal))) # ifft(fft()) = original signal
True
>>>
>>> N = len(fourier)
>>> signal = empty(N,complex)
>>> for k in range(N): # equivalent but much slower
... signal[k] = sum(fourier * exp(+1j*2*pi*k*arange(N)/N)) / N
See also: fft, fftfreq, fftshift


imag


>>> from numpy import *
>>> a = array([1+2j,3+4j,5+6j])
>>> a.imag
array([ 2., 4., 6.])
>>> a.imag = 9
>>> a
array([ 1.+9.j, 3.+9.j, 5.+9.j])
>>> a.imag = array([9,8,7])
>>> a
array([ 1.+9.j, 3.+8.j, 5.+7.j])
See also: real, angle


index_exp[]


>>> from numpy import *
>>> myslice = index_exp[2:4,...,4,::-1] # myslice could now be passed to a function, for example.
>>> print myslice
(slice(2, 4, None), Ellipsis, 4, slice(None, None, -1))
See also: slice, s_


indices()


>>> from numpy import *
>>> indices((2,3))
array([[[0, 0, 0],
        [1, 1, 1]],
       [[0, 1, 2],
        [0, 1, 2]]])
>>> a = array([ [ 0, 1, 2, 3, 4],
... [10,11,12,13,14],
... [20,21,22,23,24],
... [30,31,32,33,34] ])
>>> i,j = indices((2,3))
>>> a[i,j]
array([[ 0, 1, 2],
       [10, 11, 12]])
See also: mgrid, [], ix_, slice


inf


>>> from numpy import *
>>> exp(array([1000.])) # inf = infinite = number too large to represent, machine dependent
array([ inf])
>>> x = array([2,-inf,1,inf])
>>> isfinite(x) # show which elements are not nan/inf/-inf
array([True, False, True, False], dtype=bool)
>>> isinf(x) # show which elements are inf/-inf
array([False, True, False, True], dtype=bool)
>>> isposinf(x) # show which elements are inf
array([False, False, False, True], dtype=bool)
>>> isneginf(x) # show which elements are -inf
array([False, True, False, False], dtype=bool)
>>> nan_to_num(x) # replace -inf/inf with most negative/positive representable number
array([ 2.00000000e+000, -1.79769313e+308, 1.00000000e+000,
         1.79769313e+308])
See also: nan, finfo


inner()


>>> from numpy import *
>>> x = array([1,2,3])
>>> y = array([10,20,30])
>>> inner(x,y) # 1x10+2x20+3x30 = 140
140
See also: cross, outer, dot


insert()


>>> from numpy import *
>>> a = array([10,20,30,40])
>>> insert(a,[1,3],50) # insert value 50 before elements [1] and [3]
array([10, 50, 20, 30, 50, 40])
>>> insert(a,[1,3],[50,60]) # insert value 50 before element [1] and value 60 before element [3]
array([10, 50, 20, 30, 60, 40])
>>> a = array([[10,20,30],[40,50,60],[70,80,90]])
>>> insert(a, [1,2], 100, axis=0) # insert row with values 100 before row[1] and before row[2]
array([[ 10, 20, 30],
       [100, 100, 100],
       [ 40, 50, 60],
       [100, 100, 100],
       [ 70, 80, 90]])
>>> insert(a, [0,1], [[100],[200]], axis=0)
array([[100, 100, 100],
       [ 10, 20, 30],
       [200, 200, 200],
       [ 40, 50, 60],
       [ 70, 80, 90]])
>>> insert(a, [0,1], [100,200], axis=1)
array([[100, 10, 200, 20, 30],
       [100, 40, 200, 50, 60],
       [100, 70, 200, 80, 90]])
See also: delete, append


inv()


>>> from numpy import *
>>> from numpy.linalg import inv
>>> a = array([[3,1,5],[1,0,8],[2,1,4]])
>>> print a
[[3 1 5]
 [1 0 8]
 [2 1 4]]
>>> inva = inv(a) # Inverse matrix
>>> print inva
[[ 1.14285714 -0.14285714 -1.14285714]
 [-1.71428571 -0.28571429 2.71428571]
 [-0.14285714 0.14285714 0.14285714]]
>>> dot(a,inva) # Check the result, should be eye(3) within machine precision
array([[ 1.00000000e-00, 2.77555756e-17, 3.60822483e-16],
       [ 0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       [ -1.11022302e-16, 0.00000000e+00, 1.00000000e+00]])
See also: solve, pinv, det


iscomplex()


>>> import numpy as np
>>> a = np.array([1,2,3.j])
>>> np.iscomplex(a)
array([False, False, True], dtype=bool)

iscomplexobj()


>>> import numpy as np
>>> a = np.array([1,2,3.j])
>>> np.iscomplexobj(a)
True
>>> a = np.array([1,2,3])
>>> np.iscomplexobj(a)
False
>>> a = np.array([1,2,3], dtype=np.complex)
>>> np.iscomplexobj(a)
True

item()


>>> from numpy import *
>>> a = array([5])
>>> type(a[0])
<type 'numpy.int32'>
>>> a.item() # Conversion of array of size 1 to Python scalar
5
>>> type(a.item())
<type 'int'>
>>> b = array([2,3,4])
>>> b[1].item() # Conversion of 2nd element to Python scalar
3
>>> type(b[1].item())
<type 'int'>
>>> b.item(2) # Return 3rd element converted to Python scalar
4
>>> type(b.item(2))
<type 'int'>
>>> type(b[2]) # b[2] is slower than b.item(2), and there is no conversion
<type 'numpy.int32'>
See also: []


ix_()


>>> from numpy import *
>>> a = arange(9).reshape(3,3)
>>> print a
[[0 1 2]
 [3 4 5]
 [6 7 8]]
>>> indices = ix_([0,1,2],[1,2,0]) # trick to be used with array broadcasting
>>> print indices
(array([[0],
       [1],
       [2]]), array([[1, 2, 0]]))
>>> print a[indices]
[[1 2 0]
 [4 5 3]
 [7 8 6]]
>>> # The latter array is the cross-product:
>>> # [[ a[0,1] a[0,2] a[0,0]]
... # [ a[1,1] a[1,2] a[1,0]]
... # [ a[2,1] a[2,2] a[2,0]]]
...
See also: [], indices, cross, outer


lexsort()


>>> from numpy import *
>>> serialnr = array([1023, 5202, 6230, 1671, 1682, 5241])
>>> height = array([40., 42., 60., 60., 98., 40.])
>>> width = array([50., 20., 70., 60., 15., 30.])
>>>
>>> # We want to sort the serial numbers with increasing height, _AND_
>>> # serial numbers with equal heights should be sorted with increasing width.
>>>
>>> indices = lexsort(keys = (width, height)) # mind the order!
>>> indices
array([5, 0, 1, 3, 2, 4])
>>> for n in indices:
... print serialnr[n], height[n], width[n]
...
5241 40.0 30.0
1023 40.0 50.0
5202 42.0 20.0
1671 60.0 60.0
6230 60.0 70.0
1682 98.0 15.0
>>>
>>> a = vstack([serialnr,width,height]) # Alternatively: all data in one big matrix
>>> print a # Mind the order of the rows!
[[ 1023. 5202. 6230. 1671. 1682. 5241.]
 [ 50. 20. 70. 60. 15. 30.]
 [ 40. 42. 60. 60. 98. 40.]]
>>> indices = lexsort(a) # Sort on last row, then on 2nd last row, etc.
>>> a.take(indices, axis=-1)
array([[ 5241., 1023., 5202., 1671., 6230., 1682.],
       [ 30., 50., 20., 60., 70., 15.],
       [ 40., 40., 42., 60., 60., 98.]])
See also: sort, argsort


linspace()


>>> from numpy import *
>>> linspace(0,5,num=6) # 6 evenly spaced numbers between 0 and 5 incl.
array([ 0., 1., 2., 3., 4., 5.])
>>> linspace(0,5,num=10) # 10 evenly spaced numbers between 0 and 5 incl.
array([ 0. , 0.55555556, 1.11111111, 1.66666667, 2.22222222,
        2.77777778, 3.33333333, 3.88888889, 4.44444444, 5. ])
>>> linspace(0,5,num=10,endpoint=False) # 10 evenly spaced numbers between 0 and 5 EXCL.
array([ 0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
>>> stepsize = linspace(0,5,num=10,endpoint=False,retstep=True) # besides the usual array, also return the step size
>>> stepsize
(array([ 0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5]), 0.5)
>>> myarray, stepsize = linspace(0,5,num=10,endpoint=False,retstep=True)
>>> stepsize
0.5
See also: arange, logspace, r_


loadtxt()


>>> from numpy import *
>>>
>>> data = loadtxt("myfile.txt") # myfile.txt contains 4 columns of numbers
>>> t,z = data[:,0], data[:,3] # data is 2D numpy array
>>>
>>> t,x,y,z = loadtxt("myfile.txt", unpack=True) # to unpack all columns
>>> t,z = loadtxt("myfile.txt", usecols = (0,3), unpack=True) # to select just a few columns
>>> data = loadtxt("myfile.txt", skiprows = 7) # to skip 7 rows from top of file
>>> data = loadtxt("myfile.txt", comments = '!') # use '!' as comment char instead of '#'
>>> data = loadtxt("myfile.txt", delimiter=';') # use ';' as column separator instead of whitespace
>>> data = loadtxt("myfile.txt", dtype = int) # file contains integers instead of floats
See also: savetxt, fromfile


logical_and()


>>> from numpy import *
>>> logical_and(array([0,0,1,1]), array([0,1,0,1]))
array([False, False, False, True], dtype=bool)
>>> logical_and(array([False,False,True,True]), array([False,True,False,True]))
array([False, False, False, True], dtype=bool)
See also: logical_or, logical_not, logical_xor, bitwise_and


logical_not()


>>> from numpy import *
>>> logical_not(array([0,1]))
>>> logical_not(array([False,True]))
See also: logical_or, logical_not, logical_xor, bitwise_and


logical_or()


>>> from numpy import *
>>> logical_or(array([0,0,1,1]), array([0,1,0,1]))
>>> logical_or(array([False,False,True,True]), array([False,True,False,True]))
See also: logical_and, logical_not, logical_xor, bitwise_or


logical_xor()


>>> from numpy import *
>>> logical_xor(array([0,0,1,1]), array([0,1,0,1]))
>>> logical_xor(array([False,False,True,True]), array([False,True,False,True]))
See also: logical_or, logical_not, logical_or, bitwise_xor


logspace()


>>> from numpy import *
>>> logspace(-2, 3, num = 6) # 6 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 incl.
array([ 1.00000000e-02, 1.00000000e-01, 1.00000000e+00,
         1.00000000e+01, 1.00000000e+02, 1.00000000e+03])
>>> logspace(-2, 3, num = 10) # 10 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 incl.
array([ 1.00000000e-02, 3.59381366e-02, 1.29154967e-01,
         4.64158883e-01, 1.66810054e+00, 5.99484250e+00,
         2.15443469e+01, 7.74263683e+01, 2.78255940e+02,
         1.00000000e+03])
>>> logspace(-2, 3, num = 6, endpoint=False) # 6 evenly spaced pts on a logarithmic scale, from 10^{-2} to 10^3 EXCL.
array([ 1.00000000e-02, 6.81292069e-02, 4.64158883e-01,
         3.16227766e+00, 2.15443469e+01, 1.46779927e+02])
>>> exp(linspace(log(0.01), log(1000), num=6, endpoint=False)) # for comparison
array([ 1.00000000e-02, 6.81292069e-02, 4.64158883e-01,
         3.16227766e+00, 2.15443469e+01, 1.46779927e+02])
See also: arange, linspace, r_


lstsq()

lstsq() is most often used in the context of least-squares fitting of data. Suppose you obtain some noisy data y as a function of a variable t, e.g. velocity as a function of time. You can use lstsq() to fit a model to the data, if the model is linear in its parameters, that is if

y = p0 * f0(t) + p1 * f1(t) + ... + pN-1 * fN-1(t) + noise

where the pi are the parameters you want to obtain through fitting and the fi(t) are known functions of t. What follows is an example how you can do this.

First, for the example's sake, some data is simulated:


>>> from numpy import *
>>> from numpy.random import normal
>>> t = arange(0.0, 10.0, 0.05) # independent variable
>>> y = 2.0 * sin(2.*pi*t*0.6) + 2.7 * cos(2.*pi*t*0.6) + normal(0.0, 1.0, len(t))
We would like to fit this data with: model(t) = p0 * sin(2.*pi*t*0.6) + p1 * cos(2.*pi*t*0.6), where p0 and p1 are the unknown fit parameters. Here we go:


>>> from numpy.linalg import lstsq
>>> Nparam = 2 # we want to estimate 2 parameters: p_0 and p_1
>>> A = zeros((len(t),Nparam), float) # one big array with all the f_i(t)
>>> A[:,0] = sin(2.*pi*t*0.6) # f_0(t) stored
>>> A[:,1] = cos(2.*pi*t*0.6) # f_1(t) stored
>>> (p, residuals, rank, s) = lstsq(A,y)
>>> p # our final estimate of the parameters using noisy data
array([ 1.9315685 , 2.71165171])
>>> residuals # sum of the residuals: sum((p[0] * A[:,0] + p[1] * A[:,1] - y)**2)
array([ 217.23783374])
>>> rank # rank of the array A
2
>>> s # singular values of A
array([ 10., 10.])
See also: pinv, polyfit, solve


mat()


>>> from numpy import *
>>> mat('1 3 4; 5 6 9') # matrices are always 2-dimensional
matrix([[1, 3, 4],
       [5, 6, 9]])
>>> a = array([[1,2],[3,4]])
>>> m = mat(a) # convert 2-d array to matrix
>>> m
matrix([[1, 2],
       [3, 4]])
>>> a[0] # result is 1-dimensional
array([1, 2])
>>> m[0] # result is 2-dimensional
matrix([[1, 2]])
>>> a.ravel() # result is 1-dimensional
array([1, 2, 3, 4])
>>> m.ravel() # result is 2-dimensional
matrix([[1, 2, 3, 4]])
>>> a*a # element-by-element multiplication
array([[ 1, 4],
       [ 9, 16]])
>>> m*m # (algebraic) matrix multiplication
matrix([[ 7, 10],
       [15, 22]])
>>> a**3 # element-wise power
array([[ 1, 8],
       [27, 64]])
>>> m**3 # matrix multiplication m*m*m
matrix([[ 37, 54],
       [ 81, 118]])
>>> m.T # transpose of the matrix
matrix([[1, 3],
       [2, 4]])
>>> m.H # conjugate transpose (differs from .T for complex matrices)
matrix([[1, 3],
       [2, 4]])
>>> m.I # inverse matrix
matrix([[-2. , 1. ],
       [ 1.5, -0.5]])
See also: bmat, array, dot, asmatrix


matrix()


>>> from numpy import *
>>> matrix('1 3 4; 5 6 9') # matrix is synonymous with mat
matrix([[1, 3, 4],
       [5, 6, 9]])
See also: mat, asmatrix


max()


>>> from numpy import *
>>> a = array([10,20,30])
>>> a.max()
30
>>> a = array([[10,50,30],[60,20,40]])
>>> a.max()
60
>>> a.max(axis=0) # for each of the columns, find the maximum
array([60, 50, 40])
>>> a.max(axis=1) # for each of the rows, find the maximum
array([50, 60])
>>> max(a) # also exists, but is slower
See also: nan, argmax, maximum, ptp


maximum()


>>> from numpy import *
>>> a = array([1,0,5])
>>> b = array([3,2,4])
>>> maximum(a,b) # element-by-element comparison
array([3, 2, 5])
>>> max(a.tolist(),b.tolist()) # standard Python function does not give the same!
[3, 2, 4]
See also: minimum, max, argmax


mean()


>>> from numpy import *
>>> a = array([1,2,7])
>>> a.mean()
3.3333333333333335
>>> a = array([[1,2,7],[4,9,6]])
>>> a.mean()
4.833333333333333
>>> a.mean(axis=0) # the mean of each of the 3 columns
array([ 2.5, 5.5, 6.5])
>>> a.mean(axis=1) # the mean of each of the 2 rows
array([ 3.33333333, 6.33333333])
See also: average, median, var, std, sum


median()


>>> from numpy import *
>>> a = array([1,2,3,4,9])
>>> median(a)
3
>>> a = array([1,2,3,4,9,0])
>>> median(a)
2.5
See also: average, mean, var, std


mgrid[]


>>> from numpy import *
>>> m = mgrid[1:3,2:5] # rectangular mesh grid with x-values [1,2] and y-values [2,3,4]
>>> print m
[[[1 1 1]
  [2 2 2]]
 [[2 3 4]
  [2 3 4]]]
>>> m[0,1,2] # x-value of grid point with index coordinates (1,2)
2
>>> m[1,1,2] # y-value of grid point with index coordinates (1,2)
4
See also: indices, ogrid


min()


>>> from numpy import *
>>> a = array([10,20,30])
>>> a.min()
10
>>> a = array([[10,50,30],[60,20,40]])
>>> a.min()
10
>>> a.min(axis=0) # for each of the columns, find the minimum
array([10, 20, 30])
>>> a.min(axis=1) # for each of the rows, find the minimum
array([10, 20])
>>> min(a) # also exists, but is slower
See also: nan, max, minimum, argmin, ptp


minimum()


>>> from numpy import *
>>> a = array([1,0,5])
>>> b = array([3,2,4])
>>> minimum(a,b) # element-by-element comparison
array([1, 0, 4])
>>> min(a.tolist(),b.tolist()) # Standard Python function does not give the same!
[1, 0, 5]
See also: min, maximum, argmin


multiply()


>>> from numpy import *
>>> multiply(array([3,6]), array([4,7]))
array([12, 42])
See also: dot


nan


>>> from numpy import *
>>> sqrt(array([-1.0]))
array([ nan]) # nan = NaN = Not A Number
>>> x = array([2, nan, 1])
>>> isnan(x) # show which elements are nan
array([False, True, False], dtype=bool)
>>> isfinite(x) # show which elements are not nan/inf/-inf
array([True, False, True], dtype=bool)
>>> nansum(x) # same as sum() but ignore nan elements
3.0
>>> nanmax(x) # same as max() but ignore nan elements
2.0
>>> nanmin(x) # same as min() but ignore nan elements
1.0
>>> nanargmin(x) # same as argmin() but ignore nan elements
2
>>> nanargmax(x) # same as argmax() but ignore nan elements
0
>>> nan_to_num(x) # replace all nan elements with 0.0
array([ 2., 0., 1.])
See also: inf


ndenumerate()


>>> from numpy import *
>>> a = arange(9).reshape(3,3) + 10
>>> a
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
>>> b = ndenumerate(a)
>>> for position,value in b: print position,value # position is the N-dimensional index
...
(0, 0) 10
(0, 1) 11
(0, 2) 12
(1, 0) 13
(1, 1) 14
(1, 2) 15
(2, 0) 16
(2, 1) 17
(2, 2) 18
See also: broadcast, ndindex


ndim


>>> from numpy import *
>>> a = arange(12).reshape(3,4)
>>> a
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])
>>> a.ndim # a has 2 axes
2
>>> a.shape = (2,2,3)
array([[[ 0, 1, 2],
        [ 3, 4, 5]],
       [[ 6, 7, 8],
        [ 9, 10, 11]]])
>>> a.ndim # now a has 3 axes
3
>>> len(a.shape) # same as ndim
3
See also: shape


ndindex()


>>> for index in ndindex(4,3,2):
        print index
(0,0,0)
(0,0,1)
(0,1,0)
...
(3,1,1)
(3,2,0)
(3,2,1)
See also: broadcast, ndenumerate


newaxis


>>> from numpy import *
>>> x = arange(3)
>>> x
array([0, 1, 2])
>>> x[:,newaxis] # add a new dimension/axis
array([[0],
       [1],
       [2]])
>>> x[:,newaxis,newaxis] # add two new dimensions/axes
array([[[0]],
       [[1]],
       [[2]]])
>>> x[:,newaxis] * x
array([[0, 0, 0],
       [0, 1, 2],
       [0, 2, 4]])
>>> y = arange(3,6)
>>> x[:,newaxis] * y # outer product, same as outer(x,y)
array([[ 0, 0, 0],
       [ 3, 4, 5],
       [ 6, 8, 10]])
>>> x.shape
(3,)
>>> x[newaxis,:].shape # x[newaxis,:] is equivalent to x[newaxis] and x[None]
(1,3)
>>> x[:,newaxis].shape
(3,1)
See also: [], atleast_1d, atleast_2d, atleast_3d, expand_dims


nonzero()


>>> from numpy import *
>>> x = array([1,0,2,-1,0,0,8])
>>> indices = x.nonzero() # find the indices of the nonzero elements
>>> indices
(array([0, 2, 3, 6]),)
>>> x[indices]
array([1, 2, -1, 8])
>>> y = array([[0,1,0],[2,0,3]])
>>> indices = y.nonzero()
>>> indices
(array([0, 1, 1]), array([1, 0, 2]))
>>> y[indices[0],indices[1]] # one way of doing it, explains what's in indices[0] and indices[1]
array([1, 2, 3])
>>> y[indices] # this way is shorter
array([1, 2, 3])
>>> y = array([1,3,5,7])
>>> indices = (y >= 5).nonzero()
>>> y[indices]
array([5, 7])
>>> nonzero(y) # function also exists
(array([0, 1, 2, 3]),)
See also: [], where, compress, choose, take


ogrid()


>>> from numpy import *
>>> x,y = ogrid[0:3,0:3] # x and y are useful to use with broadcasting rules
>>> x
array([[0],
       [1],
       [2]])
>>> y
array([[0, 1, 2]])
>>> print x*y # example how to use broadcasting rules
[[0 0 0]
 [0 1 2]
 [0 2 4]]
See also: mgrid


ones()


>>> from numpy import *
>>> ones(5)
array([ 1., 1., 1., 1., 1.])
>>> ones((2,3), int)
array([[1, 1, 1],
       [1, 1, 1]])
See also: ones_like, zeros, empty, eye, identity


ones_like()


>>> from numpy import *
>>> a = array([[1,2,3],[4,5,6]])
>>> ones_like(a) # ones initialised array with the same shape and datatype as 'a'
array([[1, 1, 1],
       [1, 1, 1]])
See also: ones, zeros_like


outer()


>>> from numpy import *
>>> x = array([1,2,3])
>>> y = array([10,20,30])
>>> outer(x,y) # outer product
array([[10, 20, 30],
       [20, 40, 60],
       [30, 60, 90]])
See also: inner, cross


permutation()


>>> from numpy import *
>>> from numpy.random import permutation
>>> permutation(4) # permutation of integers from 0 to 3
array([0, 3, 1, 2])
>>> permutation(4) # another permutation of integers from 0 to 3
array([2, 1, 0, 3])
>>> permutation(4) # yet another permutation of integers from 0 to 3
array([3, 0, 2, 1])
See also: shuffle, bytes, seed


piecewise()


>>> from numpy import *
>>> f1 = lambda x: x*x
>>> f2 = lambda x: 2*x
>>> x = arange(-2.,3.,0.1)
>>> condition = (x>1)&(x<2) # boolean array
>>> y = piecewise(x,condition, [f1,1.]) # if condition is true, return f1, otherwise 1.
>>> y = piecewise(x, fabs(x)<=1, [f1,0]) + piecewise(x, x>1, [f2,0]) # 0. in ]-inf,-1[, f1 in [-1,+1], f2 in ]+1,+inf[
>>> print y
<snip>
See also: select


pinv()


>>> from numpy import *
>>> from numpy.linalg import pinv,svd,lstsq
>>> A = array([[1., 3., 5.],[2., 4., 6.]])
>>> b = array([1., 3.])
>>>
>>> # Question: find x such that ||A*x-b|| is minimal
>>> # Answer: x = pinvA * b, with pinvA the pseudo-inverse of A
>>>
>>> pinvA = pinv(A)
>>> print pinvA
[[-1.33333333 1.08333333]
 [-0.33333333 0.33333333]
 [ 0.66666667 -0.41666667]]
>>> x = dot(pinvA, b)
>>> print x
[ 1.91666667 0.66666667 -0.58333333]
>>>
>>> # Relation with least-squares minimisation lstsq()
>>>
>>> x,resids,rank,s = lstsq(A,b)
>>> print x # the same solution for x as above
[ 1.91666667 0.66666667 -0.58333333]
>>>
>>> # Relation with singular-value decomposition svd()
>>>
>>> U,sigma,V = svd(A)
>>> S = zeros_like(A.transpose())
>>> for n in range(len(sigma)): S[n,n] = 1. / sigma[n]
>>> dot(V.transpose(), dot(S, U.transpose())) # = pinv(A)
array([[-1.33333333, 1.08333333],
       [-0.33333333, 0.33333333],
       [ 0.66666667, -0.41666667]])
See also: inv, lstsq, solve, svd


poisson()


>>> from numpy import *
>>> from numpy.random import *
>>> poisson(lam=0.5, size=(2,3)) # poisson distribution lambda=0.5
array([[2, 0, 0],
       [1, 1, 0]])
See also: random_sample, uniform, standard_normal, seed


poly1d()


>>> from numpy import *
>>> p1 = poly1d([2,3],r=1) # specify polynomial by its roots
>>> print p1
   2
1 x - 5 x + 6
>>> p2 = poly1d([2,3],r=0) # specify polynomial by its coefficients
>>> print p2
2 x + 3
>>> print p1+p2 # +,-,*,/ and even ** are supported
   2
1 x - 3 x + 9
>>> quotient,remainder = p1/p2 # division gives a tupple with the quotient and remainder
>>> print quotient,remainder
0.5 x - 3
15
>>> p3 = p1*p2
>>> print p3
   3 2
2 x - 7 x - 3 x + 18
>>> p3([1,2,3,4]) # evaluate the polynomial in the values [1,2,3,4]
array([10, 0, 0, 22])
>>> p3[2] # the coefficient of x**2
-7
>>> p3.r # the roots of the polynomial
array([-1.5, 3. , 2. ])
>>> p3.c # the coefficients of the polynomial
array([ 2, -7, -3, 18])
>>> p3.o # the order of the polynomial
3
>>> print p3.deriv(m=2) # the 2nd derivative of the polynomial
12 x - 14
>>> print p3.integ(m=2,k=[1,2]) # integrate polynomial twice and use [1,2] as integration constants
     5 4 3 2
0.1 x - 0.5833 x - 0.5 x + 9 x + 1 x + 2

polyfit()


>>> from numpy import *
>>> x = array([1,2,3,4,5])
>>> y = array([6, 11, 18, 27, 38])
>>> polyfit(x,y,2) # fit a 2nd degree polynomial to the data, result is x**2 + 2x + 3
array([ 1., 2., 3.])
>>> polyfit(x,y,1) # fit a 1st degree polynomial (straight line), result is 8x-4
array([ 8., -4.])
See also: lstsq


prod()


>>> from numpy import *
>>> a = array([1,2,3])
>>> a.prod() # 1 * 2 * 3 = 6
6
>>> prod(a) # also exists
6
>>> a = array([[1,2,3],[4,5,6]])
>>> a.prod(dtype=float) # specify type of output
720.0
>>> a.prod(axis=0) # for each of the 3 columns: product
array([ 4, 10, 18])
>>> a.prod(axis=1) # for each of the two rows: product
array([ 6, 120])
See also: cumprod, sum


ptp()


>>> from numpy import *
>>> a = array([5,15,25])
>>> a.ptp() # peak-to-peak = maximum - minimum
20
>>> a = array([[5,15,25],[3,13,33]])
>>> a.ptp()
30
>>> a.ptp(axis=0) # peak-to-peak value for each of the 3 columns
array([2, 2, 8])
>>> a.ptp(axis=1) # peak-to-peak value for each of the 2 rows
array([20, 30])
See also: max, min


put()


>>> from nump import *
>>> a = array([10,20,30,40])
>>> a.put([60,70,80], [0,3,2]) # first values, then indices
>>> a
array([60, 20, 80, 70])
>>> a[[0,3,2]] = [60,70,80] # same effect
>>> a.put([40,50], [0,3,2,1]) # if value array is too short, it is repeated
>>> a
array([40, 50, 40, 50])
>>> put(a, [0,3], [90]) # also exists, but here FIRST indices, THEN values
>>> a
array([90, 50, 40, 90])
See also: putmask, take


putmask()


>>> from nump import *
>>> a = array([10,20,30,40])
>>> mask = array([True,False,True,True]) # size mask = size a
>>> a.putmask([60,70,80,90], mask) # first values, then the mask
>>> a
array([60, 20, 80, 90])
>>> a = array([10,20,30,40])
>>> a[mask] # reference
array([60, 80, 90])
>>> a[mask] = array([60,70,80,90]) # NOT exactly the same as putmask
>>> a
array([60, 20, 70, 80])
>>> a.putmask([10,90], mask) # if value array is too short, it is repeated
>>> a
array([10, 20, 10, 90])
>>> putmask(a, mask, [60,70,80,90]) # also exists, but here FIRST mask, THEN values
See also: put, take


r_[]


>>> from numpy import *
>>> r_[1:5] # same as arange(1,5)
array([1, 2, 3, 4])
>>> r_[1:10:4] # same as arange(1,10,4)
array([1, 5, 9])
>>> r_[1:10:4j] # same as linspace(1,10,4), 4 equally-spaced elements between 1 and 10 inclusive
array([ 1., 4., 7., 10.])
>>> r_[1:5,7,1:10:4] # sequences separated with commas are concatenated
array([1, 2, 3, 4, 7, 1, 5, 9])
>>> r_['r', 1:3] # return a matrix. If 1-d, result is a 1xN matrix
matrix([[1, 2]])
>>> r_['c',1:3] # return a matrix. If 1-d, result is a Nx1 matrix
matrix([[1],
       [2]])
>>> a = array([[1,2,3],[4,5,6]])
>>> r_[a,a] # concatenation along 1st (default) axis (row-wise, that's why it's called r_)
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
>>> r_['-1',a,a] # concatenation along last axis, same as c_[a,a]
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])
See also: c_, s_, arange, linspace, hstack, vstack, column_stack, concatenate, bmat


rand()


>>> from numpy import *
>>> from numpy.random import *
>>> rand(3,2)
array([[ 0.65159297, 0.78872335],
       [ 0.09385959, 0.02834748],
       [ 0.8357651 , 0.43276707]])
See also: random_sample, seed


randint()

Synonym for random_integers()

See random_integers


randn()


>>> randn(2,3)
array([[ 1.22497074, -0.29508896, -0.75040033],
       [-0.54822685, -0.98032155, -1.40467696]])
See also: standard_normal, poisson, seed


random_integers()


>>> from numpy import *
>>> from numpy.random import *
>>> random_integers(-1,5,(2,2))
array([[ 3, -1],
       [-1, 0]])
See also: random_sample, uniform, poisson, seed


random_sample()


>>> from numpy import *
>>> from numpy.random import *
>>> random_sample((3,2))
array([[ 0.76228008, 0.00210605],
       [ 0.44538719, 0.72154003],
       [ 0.22876222, 0.9452707 ]])
See also: ranf, sample, rand, seed


ranf()

Synonym for random_sample

See random_sample, sample


ravel()


>>> from numpy import *
>>> a = array([[1,2],[3,4]])
>>> a.ravel() # 1-d version of a
array([1, 2, 3, 4])
>>> b = a[:,0].ravel() # a[:,0] does not occupy a single memory segment, thus b is a copy, not a reference
>>> b
array([1, 3])
>>> c = a[0,:].ravel() # a[0,:] occupies a single memory segment, thus c is a reference, not a copy
>>> c
array([1, 2])
>>> b[0] = -1
>>> c[1] = -2
>>> a
array([[ 1, -2],
       [ 3, 4]])
>>> ravel(a) # also exists
See also: flatten


real


>>> from numpy import *
>>> a = array([1+2j,3+4j,5+6j])
>>> a.real
array([ 1., 3., 5.])
>>> a.real = 9
>>> a
array([ 9.+2.j, 9.+4.j, 9.+6.j])
>>> a.real = array([9,8,7])
>>> a
array([ 9.+2.j, 8.+4.j, 7.+6.j])
See also: imag, angle


recarray()


>>> from numpy import *
>>> num = 2
>>> a = recarray(num, formats='i4,f8,f8',names='id,x,y')
>>> a['id'] = [3,4]
>>> a['id']
array([3, 4])
>>> a = rec.fromrecords([(35,1.2,7.3),(85,9.3,3.2)], names='id,x,y') # fromrecords is in the numpy.rec submodule
>>> a['id']
array([35, 85])
See also: array, dtype


reduce()


>>> from numpy import *
>>> add.reduce(array([1.,2.,3.,4.])) # computes ((((1.)+2.)+3.)+4.)
10.0
>>> multiply.reduce(array([1.,2.,3.,4.])) # works also with other operands. Computes ((((1.)*2.)*3.)*4.)
24.0
>>> add.reduce(array([[1,2,3],[4,5,6]]), axis = 0) # reduce every column separately
array([5, 7, 9])
>>> add.reduce(array([[1,2,3],[4,5,6]]), axis = 1) # reduce every row separately
array([ 6, 15])
See also: accumulate, sum, prod


repeat()


>>> from numpy import *
>>> repeat(7., 4)
array([ 7., 7., 7., 7.])
>>> a = array([10,20])
>>> a.repeat([3,2])
array([10, 10, 10, 20, 20])
>>> repeat(a, [3,2]) # also exists
>>> a = array([[10,20],[30,40]])
>>> a.repeat([3,2,1,1])
array([10, 10, 10, 20, 20, 30, 40])
>>> a.repeat([3,2],axis=0)
array([[10, 20],
       [10, 20],
       [10, 20],
       [30, 40],
       [30, 40]])
>>> a.repeat([3,2],axis=1)
array([[10, 10, 10, 20, 20],
       [30, 30, 30, 40, 40]])
See also: tile


reshape()


>>> from numpy import *
>>> x = arange(12)
>>> x.reshape(3,4) # array with 3 rows and 4 columns. 3x4=12. Total number of elements is always the same.
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])
>>> x.reshape(3,2,2) # 3x2x2 array; 3x2x2 = 12. x itself does _not_ change.
array([[[ 0, 1],
        [ 2, 3]],
       [[ 4, 5],
        [ 6, 7]],
       [[ 8, 9],
        [10, 11]]])
>>> x.reshape(2,-1) # 'missing' -1 value n is calculated so that 2xn=12, so n=6
array([[ 0, 1, 2, 3, 4, 5],
       [ 6, 7, 8, 9, 10, 11]])
>>> x.reshape(12) # reshape(1,12) is not the same as reshape(12)
array([0,1,2,3,4,5,6,7,8,9,10,11])
>>> reshape(x,(2,6)) # Separate function reshape() also exists
See also: shape, resize


resize()


>>> from numpy import *
>>> a = array([1,2,3,4])
>>> a.resize(2,2) # changes shape of 'a' itself
>>> print a
[[1 2]
 [3 4]]
>>> a.resize(3,2) # reallocates memoy of 'a' to change nr of elements, fills excess elements with 0
>>> print a
[[1 2]
 [3 4]
 [0 0]]
>>> a.resize(2,4)
>>> print a
[[1 2 3 4]
 [0 0 0 0]]
>>> a.resize(2,1) # throws away elements of 'a' to fit new shape
>>> print a
[[1]
 [2]]
But, there is a caveat:




>>> b = array([1,2,3,4])
>>> c = b # c is reference to b, it doesn't 'own' its data
>>> c.resize(2,2) # no problem, nr of elements doesn't change
>>> c.resize(2,3) # doesn't work, c is only a reference
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: cannot resize an array that has been referenced or is referencing
another array in this way. Use the resize function
>>> b.resize(2,3) # doesn't work, b is referenced by another array
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: cannot resize an array that has been referenced or is referencing
another array in this way. Use the resize function
and it's not always obvious what the reference is:




>>> d = arange(4)
>>> d
array([0, 1, 2, 3])
>>> d.resize(5) # doesn't work, but where's the reference?
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: cannot resize an array that has been referenced or is referencing
another array in this way. Use the resize function
>>> _ # '_' was a reference to d!
array([0, 1, 2, 3])
>>> d = resize(d, 5) # this does work, however
>>> d
array([0, 1, 2, 3, 0])
See also: reshape


rollaxis()


>>> from numpy import *
>>> a = arange(3*4*5).reshape(3,4,5)
>>> a.shape
(3, 4, 5)
>>> b = rollaxis(a,1,0) # transpose array so that axis 1 is 'rolled' before axis 0
>>> b.shape
(4, 3, 5)
>>> b = rollaxis(a,0,2) # transpose array so that axis 0 is 'rolled' before axis 2
>>> b.shape
(4, 3, 5)
See also: swapaxes, transpose


round()

round(decimals=0, out=None) -> reference to rounded values.


>>> from numpy import *
>>> array([1.2345, -1.647]).round() # rounds the items. Type remains float64.
array([ 1., -2.])
>>> array([1, -1]).round() # integer arrays stay as they are
array([ 1, -1])
>>> array([1.2345, -1.647]).round(decimals=1) # round to 1 decimal place
array([ 1.2, -1.6])
>>> array([1.2345+2.34j, -1.647-0.238j]).round() # both real and complex parts are rounded
array([ 1.+2.j, -2.-0.j])
>>> array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]).round() # numpy rounds x.5 to nearest even.
array([ 0., 0., 1., 2., 2., 2.])
>>> a = zeros(3, dtype=int)
>>> array([1.2345, -1.647, 3.141]).round(out=a) # different output arrays may be specified
array([ 1, -2, 3])
>>> a # and the output is cast to the new type
array([ 1, -2, 3])
>>> round_(array([1.2345, -1.647])) # round_ is the functional form. -> a copy.
array([ 1., -2.])
>>> around(array([1.2345, -1.647])) # around is an alias of round_.
array([ 1., -2.])
See also: ceil, floor, fix, astype


rot90()


>>> from numpy import *
>>> a = arange(12).reshape(4,3)
>>> a
array([[ 0, 1, 2],
       [ 3, 4, 5],
       [ 6, 7, 8],
       [ 9, 10, 11]])
>>> rot90(a) # 'rotate' the matrix 90 degrees
array([[ 2, 5, 8, 11],
       [ 1, 4, 7, 10],
       [ 0, 3, 6, 9]])
See also: fliplr, flipud


s_[]


>>> from numpy import *
>>> s_[1:5] # easy slice generating. See r_[] examples.
slice(1, 5, None)
>>> s_[1:10:4]
slice(1, 10, 4)
>>> s_[1:10:4j]
slice(1, 10, 4j)
>>> s_['r',1:3] # to return a matrix. If 1-d, result is a 1xN matrix
('r', slice(1, 3, None))
>>> s_['c',1:3] # to return a matrix. If 1-d, result is a Nx1 matrix
('c', slice(1, 3, None))
See also: r_, c_, slice, index_exp


sample()

Synonym for random_sample

See also: random_sample, ranf


savetxt()


>>> from numpy import *
>>> savetxt("myfile.txt", data) # data is 2D array
>>> savetxt("myfile.txt", x) # x is 1D array. 1 column in file.
>>> savetxt("myfile.txt", (x,y)) # x,y are 1D arrays. 2 rows in file.
>>> savetxt("myfile.txt", transpose((x,y))) # x,y are 1D arrays. 2 columns in file.
>>> savetxt("myfile.txt", transpose((x,y)), fmt='%6.3f') # use new format instead of '%.18e'
>>> savetxt("myfile.txt", data, delimiter = ';') # use ';' to separate columns instead of space
See also: loadtxt, tofile


searchsorted()

searchsorted(keys, side="left")


>>> from numpy import *
>>> a = array([1,2,2,3]) # a is 1-D and in ascending order.
>>> a.searchsorted(2) # side defaults to "left"
1 # a[1] is the first element in a >= 2
>>> a.searchsorted(2, side='right') # look for the other end of the run of twos
3 # a[3] is the first element in a > 2
>>> a.searchsorted(4) # 4 is greater than any element in a
4 # the returned index is 1 past the end of a.
>>> a.searchsorted([[1,2],[2,3]]) # whoa, fancy keys
array([[0, 1], # the returned array has the same shape as the keys
       [1, 3]])
>>> searchsorted(a,2) # there is a functional form
1
See also: sort, histogram


seed()


>>> seed([1]) # seed the pseudo-random number generator
>>> rand(3)
array([ 0.13436424, 0.84743374, 0.76377462])
>>> seed([1])
>>> rand(3)
array([ 0.13436424, 0.84743374, 0.76377462])
>>> rand(3)
array([ 0.25506903, 0.49543509, 0.44949106])

select()


>>> from numpy import *
>>> x = array([5., -2., 1., 0., 4., -1., 3., 10.])
>>> select([x < 0, x == 0, x <= 5], [x-0.1, 0.0, x+0.2], default = 100.)
array([ 5.2, -2.1, 1.2, 0. , 4.2, -1.1, 3.2, 100. ])
>>>
>>> # This is how it works:
>>>
>>> result = zeros_like(x)
>>> for n in range(len(x)):
... if x[n] < 0: result[n] = x[n]-0.1 # The order of the conditions matters. The first one that
... elif x[n] == 0: result[n] = 0.0 # matches, will be 'selected'.
... elif x[n] <= 5: result[n] = x[n]+0.2
... else: result[n] = 100. # The default is used when none of the conditions match
...
>>> result
array([ 5.2, -2.1, 1.2, 0. , 4.2, -1.1, 3.2, 100. ])
See also: choose, piecewise


set_printoptions()


>>> from numpy import *
>>> x = array([pi, 1.e-200])
>>> x
array([ 3.14159265e+000, 1.00000000e-200])
>>> set_printoptions(precision=3, suppress=True) # 3 digits behind decimal point + suppress small values
>>> x
array([ 3.142, 0. ])
>>>
>>> help(set_printoptions) # see help() for keywords 'threshold','edgeitems' and 'linewidth'

shape


>>> from numpy import *
>>> x = arange(12)
>>> x.shape
(12,)
>>> x.shape = (3,4) # array with 3 rows and 4 columns. 3x4=12. Total number of elements is always the same.
>>> x
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])
>>> x.shape = (3,2,2) # 3x2x2 array; 3x2x2 = 12. x itself _does_ change, unlike reshape().
>>> x
array([[[ 0, 1],
        [ 2, 3]],
       [[ 4, 5],
        [ 6, 7]],
       [[ 8, 9],
        [10, 11]]])
>>> x.shape = (2,-1) # 'missing' -1 value n is calculated so that 2xn=12, so n=6
>>> x
array([[ 0, 1, 2, 3, 4, 5],
       [ 6, 7, 8, 9, 10, 11]])
>>> x.shape = 12 # x.shape = (1,12) is not the same as x.shape = 12
>>> x
array([0,1,2,3,4,5,6,7,8,9,10,11])
See also: reshape


shuffle()


>>> from numpy import *
>>> from numpy.random import shuffle
>>> x = array([1,50,-1,3])
>>> shuffle(x) # shuffle the elements of x
>>> print x
[-1 3 50 1]
>>> x = ['a','b','c','z']
>>> shuffle(x) # works with any sequence
>>> print x
['a', 'c', 'z', 'b']
See also: permutation, bytes


slice()


>>> s = slice(3,9,2) # slice objects exist outside numpy
>>> from numpy import *
>>> a = arange(20)
>>> a[s]
array([3, 5, 7])
>>> a[3:9:2] # same thing
array([3, 5, 7])
See also: [], ..., newaxis, s_, ix_, indices, index_exp


solve()


>>> from numpy import *
>>> from numpy.linalg import solve
>>>
>>> # The system of equations we want to solve for (x0,x1,x2):
>>> # 3 * x0 + 1 * x1 + 5 * x2 = 6
>>> # 1 * x0 + 8 * x2 = 7
>>> # 2 * x0 + 1 * x1 + 4 * x2 = 8
>>>
>>> a = array([[3,1,5],[1,0,8],[2,1,4]])
>>> b = array([6,7,8])
>>> x = solve(a,b)
>>> print x # This is our solution
[-3.28571429 9.42857143 1.28571429]
>>>
>>> dot(a,x) # Just checking if we indeed obtain the righthand side
array([ 6., 7., 8.])
See also: inv


sometrue()


>>> from numpy import *
>>> b = array([True, False, True, True])
>>> sometrue(b)
True
>>> a = array([1, 5, 2, 7])
>>> sometrue(a >= 5)
True
See also: alltrue, all, any


sort()

sort(axis=-1, kind="quicksort")


>>> from numpy import *
>>> a = array([2,0,8,4,1])
>>> a.sort() # in-place sorting with quicksort (default)
>>> a
array([0, 1, 2, 4, 8])
>>> a.sort(kind='mergesort') # algorithm options are 'quicksort', 'mergesort' and 'heapsort'
>>> a = array([[8,4,1],[2,0,9]])
>>> a.sort(axis=0)
>>> a
array([[2, 0, 1],
       [8, 4, 9]])
>>> a = array([[8,4,1],[2,0,9]])
>>> a.sort(axis=1) # default axis = -1
>>> a
array([[1, 4, 8],
       [0, 2, 9]])
>>> sort(a) # there is a functional form
See also: argsort, lexsort


split()


>>> from numpy import *
>>> a = array([[1,2,3,4],[5,6,7,8]])
>>> split(a,2,axis=0) # split a in 2 parts. row-wise
array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]
>>> split(a,4,axis=1) # split a in 4 parts, column-wise
[array([[1],
       [5]]), array([[2],
       [6]]), array([[3],
       [7]]), array([[4],
       [8]])]
>>> split(a,3,axis=1) # impossible to split in 3 equal parts -> error (SEE: array_split)
Traceback (most recent call last):
<snip>
ValueError: array split does not result in an equal division
>>> split(a,[2,3],axis=1) # make a split before the 2nd and the 3rd column
[array([[1, 2],
       [5, 6]]), array([[3],
       [7]]), array([[4],
       [8]])]
See also: dsplit, hsplit, vsplit, array_split, concatenate


squeeze()


>>> from numpy import *
>>> a = arange(6)
>>> a = a.reshape(1,2,1,1,3,1)
>>> a
array([[[[[[0],
           [1],
           [2]]]],
        [[[[3],
           [4],
           [5]]]]]])
>>> a.squeeze() # result has shape 2x3, all dimensions with length 1 are removed
array([[0, 1, 2],
       [3, 4, 5]])
>>> squeeze(a) # also exists

std()


>>> from numpy import *
>>> a = array([1.,2,7])
>>> a.std() # normalized by N (not N-1)
2.6246692913372702
>>> a = array([[1.,2,7],[4,9,6]])
>>> a.std()
2.793842435706702
>>> a.std(axis=0) # standard deviation of each of the 3 columns
array([ 1.5, 3.5, 0.5])
>>> a.std(axis=1) # standard deviation of each of the 2 columns
array([ 2.62466929, 2.05480467])
See also: mean, var, cov


standard_normal()


>>> standard_normal((2,3))
array([[ 1.12557608, -0.13464922, -0.35682992],
       [-1.54090277, 1.21551589, -1.82854551]])
See also: randn, uniform, poisson, seed


sum()


>>> from numpy import *
>>> a = array([1,2,3])
>>> a.sum()
6
>>> sum(a) # also exists
>>> a = array([[1,2,3],[4,5,6]])
>>> a.sum()
21
>>> a.sum(dtype=float) # specify type of output
21.0
>>> a.sum(axis=0) # sum over rows for each of the 3 columns
array([5, 7, 9])
>>> a.sum(axis=1) # sum over columns for each of the 2 rows
array([ 6, 15])
See also: accumulate, nan, cumsum, prod


svd()


>>> from numpy import *
>>> from numpy.linalg import svd
>>> A = array([[1., 3., 5.],[2., 4., 6.]]) # A is a (2x3) matrix
>>> U,sigma,V = svd(A)
>>> print U # U is a (2x2) unitary matrix
[[-0.61962948 -0.78489445]
 [-0.78489445 0.61962948]]
>>> print sigma # non-zero diagonal elements of Sigma
[ 9.52551809 0.51430058]
>>> print V # V is a (3x3) unitary matrix
[[-0.2298477 -0.52474482 -0.81964194]
 [ 0.88346102 0.24078249 -0.40189603]
 [ 0.40824829 -0.81649658 0.40824829]]
>>> Sigma = zeros_like(A) # constructing Sigma from sigma
>>> n = min(A.shape)
>>> Sigma[:n,:n] = diag(sigma)
>>> print dot(U,dot(Sigma,V)) # A = U * Sigma * V
[[ 1. 3. 5.]
 [ 2. 4. 6.]]
See also: pinv


swapaxes()


>>> from numpy import *
>>> a = arange(30)
>>> a = a.reshape(2,3,5)
>>> a
array([[[ 0, 1, 2, 3, 4],
        [ 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14]],
       [[15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]])
>>> b = a.swapaxes(1,2) # swap the 2nd and the 3rd axis
>>> b
array([[[ 0, 5, 10],
        [ 1, 6, 11],
        [ 2, 7, 12],
        [ 3, 8, 13],
        [ 4, 9, 14]],
       [[15, 20, 25],
        [16, 21, 26],
        [17, 22, 27],
        [18, 23, 28],
        [19, 24, 29]]])
>>> b.shape
(2, 5, 3)
>>> b[0,0,0] = -1 # be aware that b is a reference, not a copy
>>> print a[0,0,0]
See also: transpose, rollaxis


T


>>> from numpy import *
>>> x = array([[1.,2.],[3.,4.]])
>>> x
array([[ 1., 2.],
       [ 3., 4.]])
>>> x.T # shortcut for transpose()
array([[ 1., 3.],
       [ 2., 4.]])
See also: transpose


take()


>>> from numpy import *
>>> a= array([10,20,30,40])
>>> a.take([0,0,3]) # [0,0,3] is a set of indices
array([10, 10, 40])
>>> a[[0,0,3]] # the same effect
array([10, 10, 40])
>>> a.take([[0,1],[0,1]]) # shape of return array depends on shape of indices array
array([[10, 20],
       [10, 20]])
>>> a = array([[10,20,30],[40,50,60]])
>>> a.take([0,2],axis=1)
array([[10, 30],
       [40, 60]])
>>> take(a,[0,2],axis=1) # also exists
See also: [], put, putmask, compress, choose


tensordot()


>>> from numpy import *
>>> a = arange(60.).reshape(3,4,5)
>>> b = arange(24.).reshape(4,3,2)
>>> c = tensordot(a,b, axes=([1,0],[0,1])) # sum over the 1st and 2nd dimensions
>>> c.shape
(5,2)
>>> # A slower but equivalent way of computing the same:
>>> c = zeros((5,2))
>>> for i in range(5):
... for j in range(2):
... for k in range(3):
... for n in range(4):
... c[i,j] += a[k,n,i] * b[n,k,j]
...
See also: dot


tile()


>>> from numpy import *
>>> a = array([10,20])
>>> tile(a, (3,2)) # concatenate 3x2 copies of a together
array([[10, 20, 10, 20],
       [10, 20, 10, 20],
       [10, 20, 10, 20]])
>>> tile(42.0, (3,2)) # works for scalars, too
array([[ 42., 42.],
       [ 42., 42.],
       [ 42., 42.]])
>>> tile([[1,2],[4,8]], (2,3)) # works for 2-d arrays and list literals, too
array([[1, 2, 1, 2, 1, 2],
       [4, 8, 4, 8, 4, 8],
       [1, 2, 1, 2, 1, 2],
       [4, 8, 4, 8, 4, 8]])
See also: hstack, vstack, r_, c_, concatenate, repeat


tofile()


>>> from numpy import *
>>> x = arange(10.)
>>> y = x**2
>>> y.tofile("myfile.dat") # binary format
>>> y.tofile("myfile.txt", sep=' ', format = "%e") # ascii format, one row, exp notation, values separated by 1 space
>>> y.tofile("myfile.txt", sep='\n', format = "%e") # ascii format, one column, exponential notation
See also: fromfile, loadtxt, savetxt


tolist()


>>> from numpy import *
>>> a = array([[1,2],[3,4]])
>>> a.tolist() # convert to a standard python list
[[1, 2], [3, 4]]

trace()


>>> from numpy import *
>>> a = arange(12).reshape(3,4)
>>> a
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])
>>> a.diagonal()
array([ 0, 5, 10])
>>> a.trace()
15
>>> a.diagonal(offset=1)
array([ 1, 6, 11])
>>> a.trace(offset=1)
18
See also: diag, diagonal


transpose()

A very simple example:


>>> a = array([[1,2,3],[4,5,6]])
>>> print a.shape
(2, 3)
>>> b = a.transpose()
>>> print b
[[1 4]
 [2 5]
 [3 6]]
>>> print b.shape
(3, 2)
From this, a more elaborate example can be understood:


>>> a = arange(30)
>>> a = a.reshape(2,3,5)
>>> a
array([[[ 0, 1, 2, 3, 4],
        [ 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14]],
       [[15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]])
>>> b = a.transpose()
>>> b
array([[[ 0, 15],
        [ 5, 20],
        [10, 25]],
       [[ 1, 16],
        [ 6, 21],
        [11, 26]],
       [[ 2, 17],
        [ 7, 22],
        [12, 27]],
       [[ 3, 18],
        [ 8, 23],
        [13, 28]],
       [[ 4, 19],
        [ 9, 24],
        [14, 29]]])
>>> b.shape
(5, 3, 2)
>>> b = a.transpose(1,0,2) # First axis 1, then axis 0, then axis 2
>>> b
array([[[ 0, 1, 2, 3, 4],
        [15, 16, 17, 18, 19]],
       [[ 5, 6, 7, 8, 9],
        [20, 21, 22, 23, 24]],
       [[10, 11, 12, 13, 14],
        [25, 26, 27, 28, 29]]])
>>> b.shape
(3, 2, 5)
>>> b = transpose(a, (1,0,2)) # A separate transpose() function also exists
See also: T, swapaxes, rollaxis


tri()


>>> from numpy import *
>>> tri(3,4,k=0,dtype=float) # 3x4 matrix of Floats, triangular, the k=0-th diagonal and below is 1, the upper part is 0
array([[ 1., 0., 0., 0.],
       [ 1., 1., 0., 0.],
       [ 1., 1., 1., 0.]])
>>> tri(3,4,k=1,dtype=int)
array([[1, 1, 0, 0],
       [1, 1, 1, 0],
       [1, 1, 1, 1]])
See also: tril, triu


tril()


>>> from numpy import *
>>> a = arange(10,100,10).reshape(3,3)
>>> a
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])
>>> tril(a,k=0)
array([[10, 0, 0],
       [40, 50, 0],
       [70, 80, 90]])
>>> tril(a,k=1)
array([[10, 20, 0],
       [40, 50, 60],
       [70, 80, 90]])
See also: tri, triu


trim_zeros()


>>> from numpy import *
>>> x = array([0, 0, 0, 1, 2, 3, 0, 0])
>>> trim_zeros(x,'f') # remove zeros at the front
array([1, 2, 3, 0, 0])
>>> trim_zeros(x,'b') # remove zeros at the back
array([0, 0, 0, 1, 2, 3])
>>> trim_zeros(x,'bf') # remove zeros at the back and the front
array([1, 2, 3])
See also: compress


triu()


>>> from numpy import *
>>> a = arange(10,100,10).reshape(3,3)
>>> a
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])
>>> triu(a,k=0)
array([[10, 20, 30],
       [ 0, 50, 60],
       [ 0, 0, 90]])
>>> triu(a,k=1)
array([[ 0, 20, 30],
       [ 0, 0, 60],
       [ 0, 0, 0]])
See also: tri, tril


typeDict()


>>> from numpy import *
>>> typeDict['short']
<type 'numpy.int16'>
>>> typeDict['uint16']
<type 'numpy.uint16'>
>>> typeDict['void']
<type 'numpy.void'>
>>> typeDict['S']
<type 'numpy.string_'>
See also: dtype, cast


uniform()


>>> from numpy import *
>>> from numpy.random import *
>>> uniform(low=0,high=10,size=(2,3)) # uniform numbers in range [0,10)
array([[ 6.66689951, 4.50623001, 4.69973967],
       [ 6.52977732, 3.24688284, 5.01917021]])
See also: standard_normal, poisson, seed


unique()


>>> from numpy import *
>>> x = array([2,3,2,1,0,3,4,0])
>>> unique(x) # remove double values
array([0, 1, 2, 3, 4])
See also: compress, unique1d


unique1d()


>>> np.unique1d([1, 1, 2, 2, 3, 3])
array([1, 2, 3])
>>> a = np.array([[1, 1], [2, 3]])
>>> np.unique1d(a)
array([1, 2, 3])
>>> np.unique1d([1,2,6,4,2,3,2], return_index=True)
(array([1, 2, 3, 4, 6]), array([0, 1, 5, 3, 2]))
>>> x = [1,2,6,4,2,3,2]
>>> u, i = np.unique1d(x, return_inverse=True)
>>> u
array([1, 2, 3, 4, 6])
>>> i
array([0, 1, 4, 3, 1, 2, 1])
>>> [u[p] for p in i]
[1, 2, 6, 4, 2, 3, 2]
See also: compress, unique


vander()


>>> from numpy import *
>>> x = array([1,2,3,5])
>>> N=3
>>> vander(x,N) # Vandermonde matrix of the vector x
array([[ 1, 1, 1],
       [ 4, 2, 1],
       [ 9, 3, 1],
       [25, 5, 1]])
>>> column_stack([x**(N-1-i) for i in range(N)]) # to understand what a Vandermonde matrix contains
array([[ 1, 1, 1],
       [ 4, 2, 1],
       [ 9, 3, 1],
       [25, 5, 1]])

var()


>>> from numpy import *
>>> a = array([1,2,7])
>>> a.var() # normalised with N (not N-1)
6.8888888888888875
>>> a = array([[1,2,7],[4,9,6]])
>>> a.var()
7.8055555555555571
>>> a.var(axis=0) # the variance of each of the 3 columns
array([ 2.25, 12.25, 0.25])
>>> a.var(axis=1) # the variance of each of the 2 rows
array([ 6.88888889, 4.22222222])
See also: cov, std, mean


vdot()


>>> from numpy import *
>>> x = array([1+2j,3+4j])
>>> y = array([5+6j,7+8j])
>>> vdot(x,y) # conj(x) * y = (1-2j)*(5+6j)+(3-4j)*(7+8j)
(70-8j)
See also: dot, inner, cross, outer


vectorize()


>>> from numpy import *
>>> def myfunc(x):
... if x >= 0: return x**2
... else: return -x
...
>>> myfunc(2.) # works fine
4.0
>>> myfunc(array([-2,2])) # doesn't work, try it...
<snip>
>>> vecfunc = vectorize(myfunc, otypes=[float]) # declare the return type as float
>>> vecfunc(array([-2,2])) # works fine!
array([ 2., 4.])
See also: apply_along_axis, apply_over_axes


view()


>>> from numpy import *
>>> a = array([1., 2.])
>>> a.view() # new array referring to the same data as 'a'
array([ 1., 2.])
>>> a.view(complex) # pretend that a is made up of complex numbers
array([ 1.+2.j])
>>> a.view(int) # view(type) is NOT the same as astype(type)!
array([ 0, 1072693248, 0, 1073741824])
>>>
>>> mydescr = dtype({'names': ['gender','age'], 'formats': ['S1', 'i2']})
>>> a = array([('M',25),('F',30)], dtype = mydescr) # array with records
>>> b = a.view(recarray) # convert to a record array, names are now attributes
>>> >>> a['age'] # works with 'a' but not with 'b'
array([25, 30], dtype=int16)
>>> b.age # works with 'b' but not with 'a'
array([25, 30], dtype=int16)
See also: copy


vonmises()


>>> from numpy import *
>>> from numpy.random import *
>>> vonmises(mu=1,kappa=1,size=(2,3)) # Von Mises distribution mean=1.0, kappa=1
array([[ 0.81960554, 1.37470839, -0.15700173],
       [ 1.2974554 , 2.94229797, 0.32462307]])
>>> from pylab import * # histogram plot example
>>> hist(vonmises(1,1,(10000)), 50)
See also: random_sample, uniform, standard_normal, seed


vsplit()


>>> from numpy import *
>>> a = array([[1,2],[3,4],[5,6],[7,8]])
>>> vsplit(a,2) # split, row-wise, in 2 equal parts
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]])]
>>> vsplit(a,[1,2]) # split, row-wise, before row 1 and before row 2
[array([[1, 2]]), array([[3, 4]]), array([[5, 6],
       [7, 8]])]
See also: split, array_split, dsplit, hsplit, vstack


vstack()


>>> from numpy import *
>>> a =array([1,2])
>>> b = array([[3,4],[5,6]])
>>> vstack((a,b,a)) # only the first dimension of the arrays is allowed to be different
array([[1, 2],
       [3, 4],
       [5, 6],
       [1, 2]])
See also: hstack, column_stack, concatenate, dstack, vsplit


weibull()


>>> from numpy import *
>>> from numpy.random import *
>>> weibull(a=1,size=(2,3)) # I think a is the shape parameter
array([[ 0.08303065, 3.41486412, 0.67430149],
       [ 0.41383893, 0.93577601, 0.45431195]])
>>> from pylab import * # histogram plot example
>>> hist(weibull(5, (1000)), 50)
See also: random_sample, uniform, standard_normal, seed


where()


>>> from numpy import *
>>> a = array([3,5,7,9])
>>> b = array([10,20,30,40])
>>> c = array([2,4,6,8])
>>> where(a <= 6, b, c)
array([10, 20, 6, 8])
>>> where(a <= 6, b, -1)
array([10, 20, -1, -1])
>>> indices = where(a <= 6) # returns a tuple; the array contains indices.
>>> indices
(array([0, 1]),)
>>> b[indices]
array([10, 20])
>>> b[a <= 6] # an alternative syntax
array([10, 20])
>>> d = array([[3,5,7,9],[2,4,6,8]])
>>> where(d <= 6) # tuple with first all the row indices, then all the column indices
(array([0, 0, 1, 1, 1]), array([0, 1, 0, 1, 2]))
Be aware of the difference between x[list of bools] and x[list of integers]!


>>> from numpy import *
>>> x = arange(5,0,-1)
>>> print x
[5 4 3 2 1]
>>> criterion = (x <= 2) | (x >= 5)
>>> criterion
array([True, False, False, True, True], dtype=bool)
>>> indices = where(criterion, 1, 0)
>>> print indices
[1 0 0 1 1]
>>> x[indices] # integers!
array([4, 5, 5, 4, 4])
>>> x[criterion] # bools!
array([5, 2, 1])
>>> indices = where(criterion)
>>> print indices
(array([0, 3, 4]),)
>>> x[indices]
array([5, 2, 1])
See also: [], nonzero, clip


zeros()


>>> from numpy import *
>>> zeros(5)
array([ 0., 0., 0., 0., 0.])
>>> zeros((2,3), int)
array([[0, 0, 0],
       [0, 0, 0]])
See also: zeros_like, ones, empty, eye, identity


zeros_like()


>>> from numpy import *
>>> a = array([[1,2,3],[4,5,6]])
>>> zeros_like(a) # with zeros initialised array with the same shape and datatype as 'a'
array([[0, 0, 0],
       [0, 0, 0]])
See also: ones_like, zeros


CategoryCategory
Attachments
