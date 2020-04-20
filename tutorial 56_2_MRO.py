#Method Resolution Order (MRO)

class A:
    def __init__(self):
        print('init_class_A')

    def method_1(self):
        print ('method-1')


class B():
    def __init__(self):
        print('init_class_B')

    def method_2(self):
        print('method-2')


class C(A,B):
    def __init__(self):
        super().__init__() #this is the way of declaring fetching super class's constructor/arguments -- # here this will fetch class A 's constructor as class a is left parent tree (#Method Resolution Order (MRO))
        print('init_class_C')

    def method_3(self):
        print('method-3')


c1 = C() # this will execute class A's --init-- and class C's --init-- # as super() is applied in class C
print(c1.method_2()) # this will execute class B's method

print(c1.method_1()) # this will execute class A's method
print(c1.method_3()) # this will execute class C's method