#Pass Lst to the function

def Func_1(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return odd, even


lst = []
a = int(input('enter the length of list'))
for i in range(a):
    b = int(input('enter the next value:'))
    lst.append(b)
#print(lst)

result_odd, result_even = Func_1(lst)
#print(result_odd)
#print(result_even)
print(" odd num: {} , even num: {}".format(result_odd,result_even))