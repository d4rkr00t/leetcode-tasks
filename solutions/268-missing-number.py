# Missing Number
# https://leetcode.com/problems/missing-number/
# easy
#
# Tags: Amazon, Microsoft
#
# Time:  O(1)
# Space: O(1)
#
# Solution:
# TBD

from typing import List
from math import ceil


def missingNumber(nums: List[int]) -> int:
    total = ceil((len(nums) / 2) * (len(nums) + 1))
    return total - sum(nums)


print(missingNumber([3, 0, 1]), 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
