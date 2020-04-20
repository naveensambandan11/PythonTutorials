#Recursion
#Factorial using recursion

def FactRec(n):
    if n==0:
        return 1
    else:
        c = n * FactRec(n-1)
        return c

result = FactRec(5)
print(result)