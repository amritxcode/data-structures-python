def lengthOfLastWord(s):
    lst = s.split()
    
    return len(lst[-1])

print(lengthOfLastWord(" luffy is still joyboy"))