# Polymorphism - Duck Typing

class shop1:
    def offers(self):
        print('sony - 10%')
        print('lenova - 20%')

class shop2:
    def offers(self):
        print('DELL - 30%')
        print('MacBook - 5%')
        print('samsung - 20%')

class laptop:
    def infor(self,arg_1):
        arg_1.offers()  # the input arg_1 should have the same method 'offers'

#arg_1 = shop1
arg_1 = shop2() # whatever the arg_1 may vary with differnt classes, the given class should have the method 'offers'

obj_lap = laptop()
obj_lap.infor(arg_1)

