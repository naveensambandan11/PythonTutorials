#write a code to proint all values from 1 to 100. Skip the number which are divisible by 3 or 5
i = 1
while i <= 100:
    if (i % 5 != 0) and (i % 3 !=0):
        print(i)
    i = i + 1
