a = int(input('enter number:'))

if a % 2 == 0:
    print ('the given number is even')
    if a<=100:
        print('small number')
    elif 101<=a<=500:
        print('medium number')
    elif 501<=a<=1000:
        print('large number')
    else:
        print('bigger than large')

else:
    print ('the given number is odd')
