# Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# hard
#
# Tags: Google, Amazon, Microsoft
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# TBD

import bisect

def countSmaller(nums: [int]) -> [int]:
    sorted_nums = []
    res_reversed = []

    for n in reversed(nums):
        idx = bisect.bisect_left(sorted_nums, n)
        res_reversed.append(idx)
        sorted_nums.insert(idx, n)

    return res_reversed[::-1]

print(countSmaller([5,2,6,1]), [2,1,1,0])
