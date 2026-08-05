class Solution():
    def check(self,n:int, s:str) -> str:
        a = 0
        
        for i in s:
            if i == "A":
                a += 1

        if a > n/2:
            return "Anton"
        elif a < n/2:
            return "Danik"
        return "Friendship"
                            

n = int(input())
s = input()
print(Solution().check(n,s))