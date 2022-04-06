# Range Module
# https://leetcode.com/problems/range-module/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import bisect


class RangeModule:
    def __init__(self):
        self.ranges = [0, 10**9 + 1]
        self.tracked = [False, False]

    def addRange(self, left: int, right: int, track=True) -> None:
        def index(x):
            i = bisect.bisect_left(self.ranges, x)
            if self.ranges[i] != x:
                self.ranges.insert(i, x)
                self.tracked.insert(i, self.tracked[i - 1])

            return i

        i = index(left)
        j = index(right)
        self.ranges[i:j] = [left]
        self.tracked[i:j] = [track]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.ranges, left) - 1
        j = bisect.bisect_left(self.ranges, right)
        return all(self.tracked[i:j])

    def removeRange(self, left: int, right: int) -> None:
        self.addRange(left, right, False)


# add (10,20)
# ranges: [(10,20)]

# remove (14,16)
# ranges: [(10,14), (16,20)]

# remove (13,18)
# ranges: [(10,13),(18,20)]

# add (14,17)
# ranges: [(10,20)]
