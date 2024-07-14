import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
print(type(arr))

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


arr = np.array(['a', '2', '3'], dtype='i')#value error

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)