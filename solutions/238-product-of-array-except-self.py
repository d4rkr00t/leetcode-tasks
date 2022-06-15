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
    prod = []
    prev = 1
    for n in nums:
        prod.append(n * prev)
        prev = prod[-1]

    ans = [0] * len(nums)
    prev = 1
    for i in range(len(nums) - 1, -1, -1):
        cur = prev * nums[i]
        tmp = 1 if i - 1 < 0 else prod[i - 1]
        ans[i] = prev * tmp
        prev = cur

    return ans


print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

# 1   2  6 24
# 24 24 12  4
