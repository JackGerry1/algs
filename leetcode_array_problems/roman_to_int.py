def convert_roman(string):
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    for i in range(len(string)):
        if i + 1 < len(string) and roman[string[i]] < roman[string[i + 1]]:
            res -= roman[string[i]]
        else: res += roman[string[i]]
    return res

string = input("Enter a Roman Number: ")
valid_string = string.upper()
result = convert_roman(valid_string)
print(result)

