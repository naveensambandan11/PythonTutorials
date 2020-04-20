from numpy import *


arr_1 = array([[1,2,3,10],[4,5,6,20]])
print(arr_1)

print(arr_1.dtype)
print(arr_1.ndim)
print(arr_1.shape)
print(arr_1.size)

arr_2 = arr_1.flatten()
print(arr_2)
print(min(arr_2))
print(max(arr_2))

arr_3 = arr_2.reshape(4,2)
print(arr_3)

arr_4 = arr_2.reshape(2,2,2)
print(arr_4)


#matrix - creating matrix from 2D array
m1 = matrix(arr_1)  --# some issue with matrix function
print(m)

m2 = matrix(arr_2)

m3 = m1 * m2
