# Oops - object creation and execution with different inputs
class engg:

    def __init__(self,dept, sem):
        self.dept = dept
        self.sem = sem

    def student(self):
        if self.sem <=2:
            print ('student is junior',self.dept, self.sem)
        else:
            print('student is senior', self.dept, self.sem)   # class creation till this line - attributes(function __init) and method (function student)

obj_student_1 = engg('ece', 5)
obj_student_2 = engg('cse', 2)
obj_student_3 = engg('it', 1)
obj_student_4 = engg('eee',6)  # object creation - for  4 different inputs

obj_student_1.student()
obj_student_2.student()
obj_student_3.student()
obj_student_4.student() # object execution (Calling objects)
