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
    if not nums:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for n in nums[1:]:
        temp_max = max(n, max_so_far * n, min_so_far * n)
        min_so_far = min(n, max_so_far * n, min_so_far * n)

        max_so_far = temp_max

        result = max(result, max_so_far)

    return result


print(maxProduct([2, 3, -2, 4]), 6)
print(maxProduct([-2, 0, -1]), 0)
