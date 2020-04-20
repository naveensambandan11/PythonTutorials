# program to display no. of names haviong more than 5 letters

def Func_1(lst):
    name_5letters = 0
    for j in lst:
        if len(j)>=5:
            name_5letters+=1
    return name_5letters



lst = []
a = int(input('enter the length of list'))
for i in range(a):
    b = str(input('enter next value:'))
    lst.append(b)

result = Func_1(lst)
print("number of names having more than 5 letters:", result)