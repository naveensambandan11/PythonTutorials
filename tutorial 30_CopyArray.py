from audioop import avg

from numpy import *
#create array
arr_1 = arange(1,10,2)
print(arr_1)

#operations in array
arr_2 = arr_1+2
print(arr_2)

arr_3 = arr_1-1
print(arr_3)

arr_4 = arr_1*2
print(arr_4)

arr_5 = arr_4/2
print(arr_5, float)

#adding two arrays
arr_add = arr_1 + arr_2
print(arr_add)

#Maths operatoins on arrays
print(sin(arr_1))
print(cos(arr_1))
print(tan(arr_1))
print((arr_1)+2)
print(sin(arr_1)/cos(arr_1))
print(min(arr_2))
print(max(arr_2))
print(sum(arr_2))
print(average(arr_2))
print(sqrt(arr_2))
print(log(arr_2))

#concatenate two arrays
arr_conc = concatenate([arr_1,arr_2])
print(arr_conc)

arr_conc_2  = concatenate([arr_3,arr_4])
print(arr_conc_2)


#copying array
# Shallow Copy
arr_new = arr_1
print(arr_new)

print (id(arr_1))
print (id(arr_new)) # giving same memory address for source and copied

arr_new_2 = arr_2.view() # this will copy and give different memory address
print(arr_new_2)
print(id(arr_2))
print(id(arr_new_2))

#if any value in arr_2 is changed, arr_new_2 will also gets changed
arr_2[0] = 100
print(arr_new_2)


#Deep Copy
arr_new_3 = arr_3.copy()
print(arr_new_3)

arr_3[0] = 200
print (arr_new_3) # value will not change as it is deep copy

