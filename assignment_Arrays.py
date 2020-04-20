#declare array and sort it
import array as ar

x = ar.array('i',[100,201,72,81,99])
print (sorted(x))

#program to find factorial
x = int(input('enter the number:'))
temp = 1
for i in range(1, x+1):
    temp = temp*i
    print (temp)