def max_subarray():
    nums = [1, 2 ,3 ,5 ,8]
    k = 3
    left = 0
    answer = float('-inf')
    window = 0
    right = 0
    for right in range(len(nums)):
        window += nums[right]

        if right - left +1 > k:
            window -= nums[left]
            left += 1

            if right - left + 1 == k:
                answer = max(answer, window)

    return answer

print(max_subarray())