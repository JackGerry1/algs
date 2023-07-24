def merge_sort(list):
    """
    Sorts a list from smallest to largest element. 
    Returns new sorted list. 

    1st: Find midpoint of list and divide into sublists
    2nd: Recursively sort the sublists created in previous step
    3nd: Merget these sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide unsorted list at midpoint into sublists.
    Return two sublists left and right.
    """
    midpoint = len(list) // 2
    left = list[:midpoint] # go from start of list to 1 - midpoint
    right = list[midpoint:] # go from midpoint to end of list

    return left, right

def merge(left, right):
    """
    Merges to lists (arrays), sorting them in the process.
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] <= list[1] and verify_sorted(list[1:])

nums = [1, 3, 8, 2, 8, 3, 1, 8, 7, 5, 32, 8732, 8, 9, 0, 4]
l = merge_sort(nums)
print(verify_sorted(nums))
print(verify_sorted(l))
print(l)


