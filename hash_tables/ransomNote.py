class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        freq = {}
        for i in magazine:
            freq[i] = freq.get(i,0)+1
        
        for i in ransomNote:
            if freq.get(i, 0) <= 0:
                return False
            freq[i] -= 1

        return True

ransomNote = input()
magazine = input()
print(Solution().canConstruct(ransomNote, magazine))