# Polymorphism - Method Overloading

class A:

    def sum(self, a,b,c):
        D = a+b+c
        print(D)

a1 = A()
a1.sum(10,20) # this will give error as we are giving only 2 parameters instead of 3


class B:
    def sum_1(self, a = None, b = None, c = None): # here the parameters will replace this None, which is overloading

        D = 0

        if a!=None and b!=None and c!=None:
            D = a + b + c
        elif a != None and b != None:
            D = a + b
        else:
            D = a
        print(D)


b1 = B()
b1.sum_1(10, 20)
