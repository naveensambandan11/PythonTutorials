# Polymorphism - Method Overriding

class A:


    def phone(self):
        print('Nokia')

a1 = A()
a1.phone() # let this be result 1

class B(A):
    pass

a1 = B()
a1.phone() # this will show same result as result 1 as class B has no similar method as in class A. So, the clid class will execute parent class methos only.



class C(A):
    def phone(self):
        print('samsung') # this will replace result as 'samsung' as class C has similar method as in class A with new value. So, the child clss will override the parent class method -- Method Overriding

a1 = C()
a1.phone()