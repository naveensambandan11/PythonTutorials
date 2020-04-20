# Fibonacci sequence -


def Fibonacci(n):
    a = 0
    b = 1

    if n<=0:
        print('Invalid input - please enter positive number:')

    elif n == 1:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)


#n = int(input('enter the number till which you need fibonacci sequence'))

Fibonacci(int(input('enter the number till which you need fibonacci sequence')))
