# Oops - Types of Variables - class variables, instance instance
class engg:

    college = 'GTEC'  # this is class variable

    def __init__(self):
        self.name = 'baskar'
        self.dept = 'ECE'
        self.sem = 3  # these are instance variable



student_1 = engg()
student_2 = engg()
print(student_2.name, student_2.college)
print(student_1.name, student_1.college)

student_2.name = 'ram' # just changing the data in code
print(student_2.name, student_2.college)
print(student_1.name, student_1.college)

engg.college = 'VIT' # changing class variable - will be changes across all objects
print(student_2.name, student_2.college)
print(student_1.name, student_1.college)

engg.name = 'suresh' # cannot change name at class level
print(student_2.name, student_2.college)
print(student_1.name, student_1.college)


