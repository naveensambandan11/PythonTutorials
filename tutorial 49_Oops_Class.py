# Object oriented programing

# Class - design -- like blueprint
# Object - instance -- can creat object from class

class class_computer:
    def method_config(self):
        print('i5, 16gb')


object_com1 = class_computer()
object_com2 = class_computer()

# call
class_computer.method_config(object_com1)  # calling method with object 1 as argument

object_com2.method_config()  # calling method with object 2 as argument

# in-build classes in python -- ex. .append, .clear, .dtypes,
lst = [1, 2, 3, 4, 5, 6]
lst.append(7)

