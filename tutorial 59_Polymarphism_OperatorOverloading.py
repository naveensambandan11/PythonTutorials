# Polymorphism - Operator Overloading -- overload the default operators --i.e, customizing the default operators

a = 5
b = 6
print(a+b)
print(int.__add__(a,b)) # thi is the backend method for '+'
print(int.__sub__(a,b)) # thi is the backend method for '-'

c = 'naveen'
d = 'mage'
print(str.__add__(c,d))# thi is the backend method for '+' - string


class student:
    def mark(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        print(self.m1, self.m2)

    def __add__(self,other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        print('sum of m1 marks:',a1)
        print('sum of m2 marks:', a2)
        print('sum of all marks:', a1+a2)
        a3 = self.m1 + self.m2
        a4 = other.m1 + other.m2
        print('Total mark of s1:', a3)
        print('Total mark of s2:', a4)

    def __lt__(self, other):
        b1 = self.m1 + self.m2
        b2 = other.m1 + other.m2
        if b1 < b2:
            return True
        else:
            return False

    def __gt__(self,other):
        c1 = self.m1 + self.m2
        c2 = other.m1 + other.m2
        if c1 > c2:
            return True
        else:
            return False

    def __eq__(self, other):
        d1 = self.m1 + self.m2
        d2 = other.m1 + other.m2
        if d1==d2:
            return True
        else:
            return False


s1 = student()
s2 = student()

s1.mark(90,100)
s2.mark(90,100)

sum = s1 + s2 # this will not work unless __add__ method is customized in student. backend default __add__ method will not add objects
print(sum)

if s1>s2:
    print ('s1 is first') # this will not work unless __gt__ method is customized in student. backend default __gt__ method will not compare objects

elif s1<s2:
    print ('s2 is first') # this will not work unless __lt__ method is customized in student. backend default __lt__ method will not compare objects

elif s1==s2:
    print('s1 is equal to s2') # this will not work unless __eq__ method is customized in student. backend default __eq__ method will not compare objects