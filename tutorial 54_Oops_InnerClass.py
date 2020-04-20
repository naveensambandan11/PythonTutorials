# Oops - Inner Class
class univ:

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3  # these are instance variable
        self.col_details = self.college() # adding the sub class as argument

    def m_total(self):
        return self.m1 + self.m2 + self.m3
        #self.col_details.details()


    class college:   # class inside the class (sub-class)

        def __init__(self):
            self.dept = 'ECE'
            self.sem = '6th sem'

        def details(self):
            print(self.dept, self.sem)



student_1 = univ(64,85,74)
student_2 = univ(75,98,76)  # oject creation for main class

print(student_1.m_total()) # object - method calling for main class

college_1 = univ.college() # object creation for sub-class

print(college_1.details()) # object - method calling for sub-class






#other practices --



