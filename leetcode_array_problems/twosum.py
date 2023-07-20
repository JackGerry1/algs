def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum = arr[i] + arr[j]
            if sum == target:
                print(f"{arr[i]} + {arr[j]} (Solution Index {[i, j]}) = {target}") 
                return
    
array = [1, 3, 2, 8, 9, 3, 2]
target = 12

two_sum(array, target)