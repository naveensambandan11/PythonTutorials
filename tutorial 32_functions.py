#Funtion

def func_1():
    print ("hello world")

def func_2(x, y):
    sum = x+y
    print(sum)

def func_3(a, b):
    sum = a+b
    return sum

func_1()
func_2(5,6)
result = func_3(100, 200)
print(result)


def func_4(a,b,c):
    x = a+b+c
    y = (a+b)-c
    z = a-c
    return x,y,z

result_2 = func_4(5,4,2)
print(result_2)
