# Binary Search -- for searching in a big list -- to reduce run-time effort
# provide sorted list
# Define upper and lower bounds -- LB = 0, UB = len(list)-1
# Take mid of them
# compare iif the the search value is < or > to mid. - if < , change the mid as LB -- if >. change the mid as UB

pos = -1

def search(lst, n):
    lst_LB = 0
    lst_UB = len(lst)-1

    while lst_LB <= lst_UB:
        mid = (lst_LB + lst_UB) // 2

        if lst[mid] == n:
            globals()['pos'] == mid
            return True
        else:
            if lst[mid] < n:
                lst_LB = mid+1
            else:
                lst_UB = mid-1

    return False


lst = [2,3,4,5,6,7,8,75,82,91,97,156,175,242,285,374,425,435,465,524,558,585]
#n = int(input('enter the number you want to search'))
n = 2

if search(lst, n):
    print('the value is at integer position : ', pos)

else:
    print('value not found')



