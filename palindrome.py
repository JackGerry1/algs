def is_palindrome(string):
    newStr = ""

    for character in string:
        if character.isalnum():
            newStr += character.lower()

    return newStr == newStr[::-1]


# Example usage
string = "A man, a plan, a canal: Panama"

result = is_palindrome(string)
print(result)

