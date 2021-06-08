# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    ans = [0] * n
    product = [] + nums

    for i in range(n - 1)[::-1]:
        product[i] = product[i + 1] * nums[i]

    cur = 1
    for i, num in enumerate(nums):
        next = 1 if i == n - 1 else product[i + 1]
        ans[i] = cur * next
        cur = cur * num

    return ans


print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

# 1 2 6 24
