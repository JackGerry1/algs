def remove_while_loop(nums, val):    
    while val in nums:
        nums.remove(val)
    return len(nums), nums
    
def remove_for_loop(nums, val):
    for i in nums:
        if val in nums:
            nums.remove(val)
    return len(nums), nums

arr = [0,1,2,2,3,0,4,2]
val = 2
print(remove_while_loop(arr, val))
print(remove_for_loop(arr, val))