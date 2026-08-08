class Solution():
    def rotate(self, arr: list,k: int)-> int:

        k = k % len(arr)
        return arr[-k:] + arr[:-k]

arr = list(map(int, input().split(',')))
k = int(input())
print(Solution().rotate(arr, k))