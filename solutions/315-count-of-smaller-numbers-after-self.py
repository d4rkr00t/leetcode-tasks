# Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# hard
#
# Tags: Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Binary Search

from typing import List
import bisect


def countSmaller(nums: List[int]) -> List[int]:
    sorted_nums = []
    rev_result = []

    for n in reversed(nums):
        idx = bisect.bisect_left(sorted_nums, n)
        rev_result.append(idx)
        sorted_nums.insert(idx, n)

    return rev_result[::-1]


print(countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])
