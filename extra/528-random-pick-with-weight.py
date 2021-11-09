# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self.list = []
        sum = 0

        for p in w:
            self.list.append(p + sum)
            sum += p

        self.total = self.list[-1]
        print(self.list)

    def pickIndex(self) -> int:
        rnd = random.randint(1, self.total)
        pos = bisect.bisect_left(self.list, rnd, 0, len(self.list))
        return (rnd, pos)


ss = Solution([1, 3, 1])

# list  = [1,4,5]
# total = 5
#

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
