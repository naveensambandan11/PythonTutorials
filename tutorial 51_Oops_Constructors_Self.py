# Oops - object creation and execution with different inputs
class engg:

    def __init__(self):
        self.name = 'naveen'
        self.dept = 'ECE'
        self.sem = 3

    def update(self):
        self.dept = 'IT'

    def update_2(self,a):
        self.sem = a

    def compare(self,x):
        if self.name == x.name:
            print('same person')
        elif self.dept == x.dept:
            print('differnt person but same dept')
        else:
            print('completely diffenct person')


student_1 = engg()
student_2 = engg()

print(student_1.name)
print(student_1.dept)
print(student_2.name)
print(student_2.dept)
print(student_2.sem)

student_2.name = 'ram' # just changing the data in code - no methods used here

student_1.update()  # update by creating method

student_2.update_2(6) # update by creating method and passing arguments

print(student_1.name)
print(student_1.dept)
print(student_2.name)
print(student_2.dept)
print(student_2.sem)

student_1.compare(student_2)
# for another operation, creating another method and calling here by giving arguments.
# For two paraments in method (self, x), self defaults to student1 as the operation is on student1. so, declare x alone as argument,which is student_2 given here
