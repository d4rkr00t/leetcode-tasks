# Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# medium
#
# Tags: Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:
    table = {0: -1}
    ans = 0
    summ = 0

    for i, n in enumerate(nums):
        if n == k:
            ans = max(ans, 1)

        summ += n

        if summ - k in table:
            ans = max(ans, i - table[summ - k])

        if summ not in table:
            table[summ] = i

    return ans


print(maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3), 4)
print(maxSubArrayLen(nums=[-2, -1, 2, 1], k=1), 2)

# 1 -1 5 -2 -3
# 1  0 5  3  0
