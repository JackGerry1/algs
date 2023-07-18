def duplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


nums = [1, 2, 8, 3]

print(duplicate(nums))