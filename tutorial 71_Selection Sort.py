# Selection Sort
# sort by fiding minimum value in the lsit and placing it to integer 0


def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        #print(nums)  # step to check how the sort happens


nums = [7,1,8,4,6,2]

sort(nums)

print(nums)