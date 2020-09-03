# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    fp = [0] * len(nums)
    bp = [0] * len(nums)

    for i, n in enumerate(nums):
        fp[i] = fp[i-1] * n if i > 0 else n

    for i in range(len(nums) - 1, -1, -1):
        n = nums[i]
        bp[i] = bp[i+1] * n if i < len(nums) - 1 else n

    res = [0] * len(nums)

    for i in range(len(nums)):
        bef = fp[i-1] if i > 0 else 1
        aft = bp[i+1] if i < len(nums) - 1 else 1
        res[i] = bef * aft

    return res


print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

# 1   2   3   4
# 1   2   6  12
# 24 24  12   4
#
