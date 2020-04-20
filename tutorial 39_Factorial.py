# Funtion to calculate factorial
def Fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


n = int(input('enter the number to get factorial:'))

result = Fact(n)
print(result)