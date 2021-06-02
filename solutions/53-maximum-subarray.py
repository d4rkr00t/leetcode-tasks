# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# easy
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two Pointers

from typing import List


def maxSubArray(nums: List[int]) -> int:
    s = 0
    ans = float("-inf")

    for n in nums:
        s += n
        if s < n:
            s = n

        ans = max(ans, s)

    return ans


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
print(maxSubArray([-1]), -1)

# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#             ^  ^
# s = 4
