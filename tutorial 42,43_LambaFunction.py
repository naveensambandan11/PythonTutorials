#Lambda - Ananymous Function

#normal function
from functools import * # imported for the function 'reduce'


def Func_1(x,y):
    return (x*x)+y

result = Func_1(6,2)
print(result)

#simplified - using lambda
result_2 = lambda a,b : (a*a)+b
print(result_2(6,2))


# Filter, Map, Reduce

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

evens = list(filter(lambda a: a%2 == 0, lst)) # filtering even numbers using lambda
print(evens)

evens_2 = list(map(lambda b: b+2, evens)) # adding 2 to the filtered o/p
print(evens_2)

evens_3 = reduce(lambda x,y: x+y, evens_2) # sum all the numbers in evens_2 result
print(evens_3)

# another example -
nums = [1,2,3,45,6,7,98,9,4]

a = list(filter(lambda x: x%2 != 0, nums))
print(a)

b = list(map(lambda y: y/2, a))
print(b)

c = reduce(lambda x,y: (x*y)+2, b)
print(c)