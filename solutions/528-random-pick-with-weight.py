# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from bisect import bisect_left
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.arr = []
        sum = 0
        for n in w:
            sum += n
            self.arr.append(sum)

    def pickIndex(self) -> int:
        return bisect_left(self.arr, randint(1, self.arr[-1]))


ss = Solution([1, 3, 1])

print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
print(ss.pickIndex())
