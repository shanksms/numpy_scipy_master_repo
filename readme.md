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