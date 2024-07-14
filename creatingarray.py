import numpy as np
a=np.array([1,2,3])#1d array
print(a)
print(type(a)) 
#for 2d array
# b=np.array([[1,2,3],[2,3,4]])
b=np.mat([[1,2,3],[2,3,4]])
print(b)
print(type(b))
c=np.array([[[1,2,3],[1,2,3]],[[3,5,6],[2,4,7]]])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
print(c)
#for checking number of dimentions
print(a.ndim)
print(b.ndim)
print(c.ndim)

# higher dimensional arrays
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
