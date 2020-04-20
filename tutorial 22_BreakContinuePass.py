for x in range(1,100):
    if x >= 51:
        break
    print ('bus ', x)

print("Don't have more than " , x-1 , " buses")

#--------------------
for x in range(1,100):
    if x % 5 == 0:
        break
    print(x, "Buses")

#--------------------
for x in range(1,100):
    if x % 5 == 0:
       continue
    print(x, "Buses")

#--------------------
for x in range(1,100):
    if x % 5 == 0:
        pass
    print(x, "Buses")