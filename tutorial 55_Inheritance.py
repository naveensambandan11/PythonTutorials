#Inheritance

class A:
    def Method_1(self):
        print('assignment 1')

object_1 = A()
object_1.Method_1()

class B(A):
    def Method_2(self):
        print ('assignment 2')

object_2 = B()
object_2.Method_1()
object_2.Method_2() #Method_1 from Class A is also accessible here -- This is single level inheritance


class C(B):
    def Method_3(self):
        print ('assignment 3')

object_3 = C()
object_3.Method_1()
object_3.Method_2()
object_3.Method_3() #Method_1, Method_2 from Class A and B are also accessible here -- This is multi level inheritance


class D:
    def Method_4(self):
        print ('assignment 4')


class E(A,D):
    def Method_5(self):
        print ('assignment 5')

object_5 = E()
object_5.Method_1()
object_5.Method_4()
object_5.Method_5() #Method_1, Method_4 from Class A and D are also accessible here -- This is multiple inheritance



#other practice --
class univ:

    def __init__(self):
        self.m1 = 89
        self.m2 = 90
        self.m3 = 95  # these are instance variable

    def m_total(self):
        print(self.m1 + self.m2 + self.m3)


class college(univ):   # class inside the class (sub-class)

        def __init__(self):
            self.m1 = 189
            self.m2 = 190
            self.m3 = 195
            self.dept = 'ECE'
            self.sem = '6th sem'

        def details(self):
            print(self.dept, self.sem)



#student_1 = univ(64,85,74)
#student_2 = univ(75,98,76)

student_3 = univ()
print(student_3.m_total())

college_1 = college()
print(college_1.details())

college_2 = college()
print(college_2.m_total())  # accessing method from parent class

