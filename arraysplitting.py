import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array_split(a,  3)
print(b)
b=np.hsplit(a,3)
print(b)