#program to create array from user input
from array import *
array_2 = array('i',[])

num = int(input('enter the length of array:'))

for i in range(num):
    x = int(input('enter the next value:'))
    array_2.append(x)
print (array_2)

# to delete index 2 without in build fuction
for e in range(num):
    if (e==2):
        continue
    else:
        print(array_2[e])

# to reverse array without in build function -
print (array_2[::-1])

# to reverse wiythout using in build function
from array import *

array_4 = array('i', [10,20,30,40,50])
array_5 = array(array_4.typecode, [])
a = len(array_4)-1
for i in array_4:
    array_5.append(array_4[a])
    a-=1
print(array_5)
