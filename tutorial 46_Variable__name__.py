# __name__ will print as __main__ if current module is executed. And if any module is called, the __name__ given in that module will display that module's name


def Func_1 ():
    print('good moning', __name__)

Func_1()

from calc import * # this is giving __name__ as calc here. but when executed from the moduke calc, it will display __main__