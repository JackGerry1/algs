def check_anagram_builtin(x, y):
    return sorted(x) == sorted(y)

def check_anagram(x, y):
    if len(x) != len(y):
        return False
    countX = {}
    countY = {}

    for i in range(len(x)):
        countX[x[i]] = 1 + countX.get(x[i], 0)
        countY[y[i]] = 1 + countY.get(y[i], 0)
    for j in countX:
        if countX[j] != countY[j]:
            return False
    return True 

x = "aba"
y = "aab"

print(check_anagram_builtin(x, y))
print(check_anagram(x, y))