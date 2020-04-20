from numpy import *

# to add two arrays w/o in-build function
arr_1 = array([1,2,3,4,5])
arr_2 = array([10,20,30,40,50])
arr_add = zeros(len(arr_1))
for i in range(len(arr_1)):
    arr_add[i] = arr_1[i] + arr_2[i]
print(arr_add)


# to identify biggest number w/o build in function
arr_1 = array([1,2,94,103,5])
temp = arr_1[0]
for i in range(1, len(arr_1)):
    if temp < arr_1[i]:
        temp = arr_1[i]
print ('biggest number is:',temp)

# or
arr_1 = array([85,75,94,87,52])
arr_1.sort()
print('biggest number is:',arr_1[len(arr_1)-1])