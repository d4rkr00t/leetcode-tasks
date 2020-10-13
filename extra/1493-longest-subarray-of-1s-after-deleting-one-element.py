# Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# medium
#
# Tags: Yandex
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def longestSubarray(nums: List[int]) -> int:
    lo = deleted = ans = 0

    for hi, n in enumerate(nums):
        if n == 0:
            deleted += 1

        while deleted > 1:
            if nums[lo] == 0:
                deleted -= 1

            lo += 1

        ans = max(ans, hi - lo)

    if ans == len(nums):
        return ans - 1

    return ans


print(longestSubarray([1, 1, 0, 1]), 3)
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
print(longestSubarray([1, 1, 1]), 2)
print(longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]), 4)
print(longestSubarray([0, 0, 0]), 0)

# 1, 1, 0, 0, 1, 1, 1, 0, 1
# |     |
