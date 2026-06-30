

def anagram(s, t):
    if len(s) != len(t):
        return False
    check = {}
    for i in s:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
    
    for j in t:
        if j in check:
            check[j] -= 1
            if check[j] < 0:
                return False
        else:
            return False
    
    return True


print(anagram("anagram","nagaram"))