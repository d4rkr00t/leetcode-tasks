# Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import collections


def numberOfArithmeticSlices(nums: List[int]) -> int:
    ans = 0
    table = {}

    for i in range(len(nums)):
        table[i] = {}
        for j in range(i):
            delta = nums[i] - nums[j]
            sum = table[j].get(delta, 0)
            origin = table[i].get(delta, 0)
            table[i][delta] = origin + sum + 1
            ans += sum

    return ans


print(numberOfArithmeticSlices([2, 4, 6, 8, 10]), 7)
print(numberOfArithmeticSlices([7, 7, 7, 7, 7]), 16)
print(numberOfArithmeticSlices([3, -1, -5, -9]), 3)
