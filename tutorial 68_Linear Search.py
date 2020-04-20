# Linear Search

lst = [2,3,4,5,6,7,8]

pos = 0

a = int(input('enter the number you want to search'))


def search(lst, a):
    for i in range(len(lst)):
        if lst[i] == a:
            globals ()['pos'] = i
            return True



if search(lst, a):
    print('Number Found at integer position ' , pos )
else:
    print('Number not found')