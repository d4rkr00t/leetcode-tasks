# Two Sum
# https://leetcode.com/problems/two-sum/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    table = {}

    for i, n in enumerate(nums):
        if target - n in table:
            return [table[target-n], i]

        table[n] = i

    return None


print(twoSum(nums=[2, 7, 11, 15], target=9), [0, 1])
