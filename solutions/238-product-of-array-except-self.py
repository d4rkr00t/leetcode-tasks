# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ltr = [0] * n
    rtl = [0] * n

    for i in range(n):
        ltr[i] = ltr[i-1] * nums[i] if i != 0 else nums[i]
        rtl[~i] = rtl[~i+1] * nums[~i] if i != 0 else nums[~i]

    ans = [0] * n

    for i in range(n):
        l = ltr[i-1] if i-1 >= 0 else 1
        r = rtl[i+1] if i+1 < n else 1
        ans[i] = l * r

    return ans


print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

# 1  2  3  4
# 1  2  6  24
# 24 24 12 4
