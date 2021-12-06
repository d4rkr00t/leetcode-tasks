# Range Module
# https://leetcode.com/problems/range-module/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# from sortedcontainers import SortedDict


class RangeModule:
    def __init__(self):
        self.ranges = {}

    def addRange(self, left: int, right: int) -> None:
        start, end = left, right
        drop = []

        for s, e in self.ranges.items():
            if e < start:
                continue

            if s > end:
                continue

            start = min(s, start)
            end = max(e, end)

            drop.append(s)

        while drop:
            del self.ranges[drop.pop()]

        self.ranges[start] = end

    def queryRange(self, left: int, right: int) -> bool:
        for s, e in self.ranges.items():
            if s <= left and right <= e:
                return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        start, end = left, right
        drop = []

        for s, e in self.ranges.items():
            if e < start:
                continue

            if s > end:
                continue

            start = min(s, start)
            end = max(e, end)

            drop.append(s)

        while drop:
            del self.ranges[drop.pop()]

        if start < left:
            self.ranges[start] = left

        if end > right:
            self.ranges[right] = end


# []
#
# add: 10 -> 20
# [ (10->20) ]
#
# add: 15 -> 25
# [ (10->20), (15->25) ]
#
# add: 5 -> 10
# [ (5->10), (10->20), (15->25) ]
#
# remove: 14 -> 16
# [ (5->10), (10->14), (16->25) ]
#
# remove: 10 -> 14
# [ (5->10), (), (16->25) ]
#
# query: 18 -> 21
#
#
