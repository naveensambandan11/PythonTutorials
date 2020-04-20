from array import *
ar_1 = array('I', [48,80,82,75,70,72])
print(ar_1)

ar_2 = array(ar_1.typecode, (x*2 for x in ar_1))
print(ar_2)

ar_3 = array('u', ['n', 'a', 'v', 'e','e', 'n'])
print(ar_3)

ar_4 = array('u',(a for a in ar_3))
print(ar_4)

ar_5 = array(ar_1.typecode, (b**2 for b in ar_2))
print(ar_5)
#-----------------------------------------------------------

import array as ar

ar_6 = ar.array('f', (c/5 for c in ar_5))
print(ar_6)
#-----------------------------------------------------------
import array as ar

x = ar.array('i',[1,2,7,8,9])
#print (x)


y = ar.array(x.typecode,(z*3 for z in x))
#print ('new array is ', y)

newArray = ar.array(x.typecode, (a**2 for a in y))
print(newArray)

newArray_2 = ar.array('f',(b/2 for b in newArray))

print(newArray_2)