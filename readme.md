# Why Numpy array is fast?
## l = [1, 3, 4]
Because of the way the Python interpreter works, 
this is a very inefficient way to store these data points. 
First, Python lists are always lists of objects, so that the above list  is not a list of integers,
but a list of pointers to integers, which is unnecessary overhead. Additionally, 
this means that each of these lists and each of these integers ends up in a completely different,
random part of your computer’s RAM. However, modern processors actually like to retrieve things from memory in chunks, 
so this spreading of the data throughout the RAM is inefficient.
This is precisely the problem solved by the NumPy array.
# Why Use ndarrays Instead of Python Lists?
Arrays are fast because they enable vectorized operations, 
written in the low-level language C, that act on the whole array. Say you have a list and you want to multiply 
every element in the list by five. A standard Python approach would be to write a loop that iterates over the
 elements of the list and multiply each one by five. However, if your data is instead represented as an array, 
 you can multiply every element in the array by five in a single bound. Behind the scenes, the highly optimized NumPy 
 library is doing the iteration as fast as possible.
# what does np.random.seed(0) do?
it makes the output predictable
[stackoverflow link](https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do)
```python
numpy.random.seed(0) ; numpy.random.rand(4)
```
array([ 0.55,  0.72,  0.6 ,  0.54])
```python
numpy.random.seed(0) ; numpy.random.rand(4)
```
array([ 0.55,  0.72,  0.6 ,  0.54])
# Creating arrays in numpy
## Creating Arrays from Python Lists
```python
np.array([1, 4, 2, 5, 3])
```
Out[8]: array([1, 4, 2, 5, 3])
## Creating Arrays from Scratch
```python
np.zeros(10, dtype=int)
```
Out[12]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```python
np.ones((3, 5), dtype=float)
Out[13]: array([[ 1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.]])
```

```python
np.full((3, 5), 3.14)
Out[14]: array([[ 3.14,  3.14,  3.14,  3.14,  3.14],
                [ 3.14,  3.14,  3.14,  3.14,  3.14],
                [ 3.14,  3.14,  3.14,  3.14,  3.14]])
```
```python
 np.arange(0, 20, 2)
Out[15]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
```

```python
np.linspace(0, 1, 5)
Out[16]: array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
```

```python
np.eye(3)
Out[20]: array([[ 1.,  0.,  0.],
                [ 0.,  1.,  0.],
                [ 0.,  0.,  1.]])
```