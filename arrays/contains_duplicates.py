def containsDuplicate(nums):
        dups = {}
        for i in nums: 
            if i not in dups:
                dups[i] = False
            else:
                return True
        return False  
