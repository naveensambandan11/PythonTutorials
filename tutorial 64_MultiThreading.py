# MultiThreading
# Thread -- wich executed the program..
# Thread to execute in parallel -- parent thread should be divided into pieces

from threading import * # package for threading
from time import sleep   # package for sleep(wait)

class Func_1(Thread):
    def run(self):  # method name should be 'run' -- should not be changed
        for i in range(5):
            print('Welcome')
            sleep(1)


class Func_2(Thread):
    def run(self):    # method name should be 'run' -- should not be changed
        for i in range(5):
            print('Namesthe')
            sleep(1)


a1 = Func_1()
b1 = Func_2()

a1.start()   # call method 'run' as 'start' -- this is in build functionality for threading
sleep(0.2)
b1.start()

a1.join()
b1.join() # this join is to ask main thread to wait until the child threads a1 and b1 completes their jobs

print('done') # this will be executed by main thread