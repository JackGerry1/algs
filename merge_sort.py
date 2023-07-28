import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def merge_sort(values):
    if len(values) <= 1:
        return values
    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    sorted_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_values.append(left[left_index])
            left_index += 1
        else: 
            sorted_values.append(right[right_index])
            right_index += 1
    sorted_values += left[left_index:]    
    sorted_values += right[right_index:]
    return sorted_values

sorted_numbers = merge_sort(numbers)
print(sorted_numbers)