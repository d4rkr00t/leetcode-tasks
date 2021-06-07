# Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# easy
#
# Tags: Amazon
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    lo = 0
    hi = len(numbers) - 1

    while lo < hi:
        s = numbers[lo] + numbers[hi]

        if s == target:
            return [lo + 1, hi + 1]
        elif s > target:
            hi -= 1
        else:
            lo += 1

    return None


print(twoSum(numbers=[2, 7, 11, 15], target=9), [1, 2])
