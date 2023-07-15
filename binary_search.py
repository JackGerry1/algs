def binary_search(list, target):
    first_pos = 0
    last_pos = len(list) - 1
    
    while first_pos <= last_pos:
        middle_pos = (first_pos + last_pos) // 2

        if list[middle_pos] == target: 
            return middle_pos
        elif list[middle_pos] < target: 
            first_pos = middle_pos + 1
        else: 
            last_pos = middle_pos - 1
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found in list")

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    user_target = int(input("Enter a number you want to find: "))
    result = binary_search(numbers, user_target)
    verify(result)

if __name__ == "__main__":
    main()