def running_sum(nums):   
    result = 0
    run_sum = []

    for i in nums:
        result += i
        run_sum.append(result)
    return run_sum  

print(running_sum([1,2,3,4,5]))