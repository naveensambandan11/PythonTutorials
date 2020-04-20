# Oops - Types of Method - Class Method(cls), Instance method(self), Static methhod()


class engg:

    college = 'GTEC'  # this is class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3  # these are instance variable

    def m_total(self):
        return self.m1 + self.m2 + self.m3    # this is instance method

    @classmethod
    def m_college(cls):
        return cls.college  # this is class method

    @staticmethod
    def info():
        print('static variable comment')  # this is static method

    @staticmethod
    def info_2(a, b):  # any argument
        print('static variable comment', a + b) # this is static method


student_1 = engg(64,85,74)
student_2 = engg(75,98,76)

print(student_1.m_total())

print(student_1.m_college())
print(student_2.m_college())

engg.info()




#other practices --
print ('total of student 1', student_1.m_total(), engg.college)
print('avg of student 2:',(student_2.m_total())/3, engg.college)


engg.college = 'VIT'  # changing class variable here
print ('total of student 1', student_1.m_total(), engg.college)
print('avg of student 2:',(student_2.m_total())/3, engg.college)

engg.info_2(89, 90)



