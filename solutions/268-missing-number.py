# Missing Number
# https://leetcode.com/problems/missing-number/
# easy
#
# Tags: Amazon, Microsoft
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Gauss

from typing import List


def missingNumber(nums: List[int]) -> int:
    expected = len(nums) * (len(nums) + 1) // 2
    s = sum(nums)
    return expected - s


print(missingNumber([3, 0, 1]), 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
