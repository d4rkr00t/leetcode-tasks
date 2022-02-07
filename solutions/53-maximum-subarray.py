# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# easy
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxSubArray(nums: List[int]) -> int:
    s = 0
    ans = float("-inf")

    for num in nums:
        s = max(s + num, num)
        ans = max(s, ans)

    return ans


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
