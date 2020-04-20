#Local and Global Variable

#with local variable
a = 10
def Func_1():
    a = 15
    print('local:', a)
Func_1()

print('global:', a)

#w/o local variable
b = 10
def Func_2():
    print('local:', b)
Func_2()

print('global:', b)

#changing global variable from function
c = 10
def Func_3():
    global c
    c = 15
    print('local:', c)
Func_3()
print('global:', c)

#changing global variable and declaring thesame variable in the function
d = 15
def Func_4():
    d = 40
    print('local:', d)
    globals()['d'] = 50

Func_4()
print('global:',d)