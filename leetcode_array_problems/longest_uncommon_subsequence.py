def findLUSLength(a: str, b: str) -> int:
    if a == b: return -1
    
    else: return max(len(a), len(b))
    
print(findLUSLength("aba", "cdc"))
print(findLUSLength("aaa", "bbbbbbbbbdfgdfszgs"))
print(findLUSLength("aaa", "aaa"))
