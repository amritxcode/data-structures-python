def getConcatenation(nums):
    ans = [x for x in nums]

    for i in nums:
        ans.append(i)
    return ans*2

print(getConcatenation([1,2,1]))