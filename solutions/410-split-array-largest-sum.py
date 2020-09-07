# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# hard
#
# Tags: Google, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def splitArray(nums: List[int], m: int) -> int:
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

    return f[-1][-1]


print(splitArray([7, 2, 5, 10, 8], 2), 18)

#  7  9 14 24 32
# 32 25 23 18  8
#      |     |
