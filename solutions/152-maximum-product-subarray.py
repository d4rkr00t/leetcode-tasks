# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Runnig sum

from typing import List


def maxProduct(nums: List[int]) -> int:
    if not nums:
        return None

    mmin = nums[0]
    mmax = nums[0]
    ans = mmin

    for i in range(1, len(nums)):
        n = nums[i]

        prev_mmin = mmin
        mmin = min(n, mmin * n, mmax * n)
        mmax = max(n, mmax * n, prev_mmin * n)

        ans = max(ans, mmax)

    return ans


"""
-1 2 3 -2 4 -3


max = -1
min = -1

"""

print(maxProduct([2, 3, -2, 4]), 6)
print(maxProduct([-2, 0, -1]), 0)
