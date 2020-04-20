#Recursion

# Recursion - is calling function by itself
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(3000) # declaring to increase the iteration from default 1000 to 3000
i = 0
def Func_1():
    global i
    i+=1
    print('hello', i) # declaring i just to find how many iterations is going
    Func_1()

Func_1()
