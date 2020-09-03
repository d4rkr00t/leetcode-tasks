# Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:
    table = {0: -1}
    ans = acc = 0

    for i in range(len(nums)):
        acc += nums[i]

        if acc not in table:
            table[acc] = i
        if acc-k in table:
            ans = max(ans, i-table[acc-k])

    return ans


print(maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3), 4)
print(maxSubArrayLen(nums=[-2, -1, 2, 1], k=1), 2)

# 1 -1  5 -2  3
# 1  0  5  3  6
# { 2: 0, 3: 1 }

#       -2, -1, 2, 1
# sum = -1
# table = { -2: 0, 3: 0, -1: 1, 4: 1, 2: 2,  }
# ans = 1
