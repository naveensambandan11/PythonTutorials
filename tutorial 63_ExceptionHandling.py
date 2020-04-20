# Exception Handling -- Errors
#---Compile Time Error -- this is syntax error ex. missing(:)
#---Logical Error -- this is logical error -- getting wrong output
#---Run Time Error -- this is of getting error in runtime due to inputs from user. ex. diving any number by 0

#syntax:
#try:
#except exception
#finally

a =  10
b = 0  # try changing the value to any number

def Func_1():

    try:
        print('open folder/DB')  # this is for opening any folder or db in runtime to fetch data
        print(a/b)
        c = int(input('enter the new number to display'))

    except ZeroDivisionError as x:  # for error due to zero division
        print('Entering Zero will not work -- ', x)

    except ValueError as y: # for error due to invalid entry of datatype
        print('invalid datatype -- ', y)

    except Exception as z:
        print ('something went wrong -- ', z)

    finally:
        print ('close folder/DB') # this is for closing folder or db

Func_1()


