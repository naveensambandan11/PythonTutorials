# Constructor in Inheritance and Method Resolution Order
class A:
    def __init__(self):
        print('init_class_A')

    def method_1(self):
        print ('method-1')


class B(A):
    def __init__(self):
        super().__init__()     #this is the way of declaring fetching super class's constructor/arguments
        print('init_class_B')

    def method_2(self):
        print('method-2')

a1 = A()  # this will execute class A's --init--
print(a1.method_1()) # this will execute class A's method

b1 = B() # this will execute class A's --init-- and class B's --init-- # as super() is applied in class B
print(b1.method_2()) # this will execute class B's method

b2 = B() # this will execute class A's --init-- and class B's --init-- # as super() is applied in class B
print(b2.method_1())  # this will execute class A's method

