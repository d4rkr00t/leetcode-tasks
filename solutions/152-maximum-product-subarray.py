# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxProduct(nums: List[int]) -> int:
    ans = float("-inf")
    lo = 0
    hi = 0

    for n in nums:
        nhi = n * hi if hi != 0 else n
        nlo = n * lo if lo != 0 else n
        lo = min(nhi, nlo, n)
        hi = max(nhi, nlo, n)
        ans = max(ans, hi)

    return ans


print(maxProduct([2, 3, -2, 4]), 6)
print(maxProduct([-2, 0, -1]), 0)
print(maxProduct([-2, 2, 3, -2, 4, -2]), 96)

#          -2 2 3 -2 4 -2
# ans = 0   |
# lo  =  -2
# hi  =  -2
