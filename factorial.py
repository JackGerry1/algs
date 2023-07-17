def factorial(x):
    result = 1
    if x > 0:
        for i in range(1, x + 1):
            result *= i
        return result


number = int(input("Enter a number you want to find the factorial of: "))

print(factorial(number))            