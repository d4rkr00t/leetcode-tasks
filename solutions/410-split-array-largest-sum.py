# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# hard
#
# Tags: Google, Amazon, Facebook
#
# Time:  O(n^2 * m)
# Space: O(n * m)
#
# Solution:
# TBD

def splitArray(nums: [int], m: int) -> int:
    n = len(nums)
    f = [[float("inf")] * (m+1) for _ in range(n+1)]
    sub = [0] * (n+1)

    for i in range(n):
        sub[i+1] = sub[i] + nums[i]

    f[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i):
                f[i][j] = min(f[i][j], max(f[k][j-1], sub[i] - sub[k]))

    return f[n][m]

print(splitArray([7,2,5,10,8], 2), 18)
print(splitArray([1,2,3,4,5], 2), 9)
print(splitArray([1,4,4], 3), 4)
