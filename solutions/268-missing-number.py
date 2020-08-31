# Missing Number
# https://leetcode.com/problems/missing-number/
# easy
#
# Tags: Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)

    for i, x in enumerate(nums):
        n = n ^ x ^ i

    return n


print(missingNumber([3, 0, 1]), 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
