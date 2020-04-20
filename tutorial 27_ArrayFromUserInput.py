# program to create an array with input from user

from array import *
array_1 = array('f',[])

n = int(input('enter the length of arrray:'))

for i in range(n):
    x = int(input('enter the next number:'))
    array_1.append(x)
print(array_1)
y = int(input('enter the search value to get its index'))
print(array_1.index(y))
