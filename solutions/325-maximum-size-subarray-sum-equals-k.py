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
    table = {0:-1}
    s = 0
    ans = 0

    for i,n in enumerate(nums):
        s += n
        if s-k in table:
            ans = max(ans, i-table[s-k])

        table.setdefault(s, i)

    return ans


print(maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3), 4)
print(maxSubArrayLen(nums=[-2, -1, 2, 1], k=1), 2)
