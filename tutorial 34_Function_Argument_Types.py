#Funtion Argument Types

# Formal Argument and Actual Argument

def Func_1(x,y): #x and y are formal arguments
    z = x+y
    print(z)

Func_1(5,6) #5 and 6 are actual arguments
print(Func_1)


#Actual Arguments are of 4 types - position, keyword, default and variable length

def Func_2(name, age):
    print (name)
    print (age)

#position
Func_2('naveen', 30)
print(Func_2)

#keyword
Func_2(age=30, name='naveen')
print(Func_2)

#default
def Func_3(x, y=5):
    z = x+y
    return z

result = Func_3(6)
print(result)

result_2 = Func_3(6,10)
print(result_2)

#Variable Length
def Func_4(a, *b):
    print(a)
    print(b)

Func_4(1,2,3,4,5)
print(Func_4)

def Add(a, *b):
    for i in b:
        a = a+i
    print(a)

Add(1,2,3,4,5)
print(Add)

#KWargs - keyword args - advanced variable length arguments - when not sure about the argumants from user

def Fun_kwargs(name, **data):
    print(name)
    #print(data)
    for i,j in data.items():
        print (i,':',j)

Fun_kwargs('naveen', age = 30, city = 'chennai', mobile = 87381283021)
print(Fun_kwargs)