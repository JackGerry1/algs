def linear_search(list, target):
    for i in range (len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found in list")

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    user_target = int(input("Enter a number you want to find: "))
    result = linear_search(numbers, user_target)
    verify(result)

if __name__ == "__main__":
    main()