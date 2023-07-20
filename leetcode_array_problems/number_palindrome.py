def number_palindrome(x):
    x = str(x)
    newStr = ""

    for i in x:
        newStr += i.lower()
    return newStr == newStr[::-1]

num = 121

num_result = number_palindrome(num)
print(num_result)