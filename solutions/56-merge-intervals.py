# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    prev = None
    res = []

    def overlap(i1, i2):
        x1, y1 = i1
        x2, y2 = i2
        return x2 <= y1 and y2 >= x1

    for itr in intervals:
        if not prev:
            prev = itr
            continue

        if overlap(prev, itr):
            prev = [min(prev[0], itr[0]), max(prev[1], itr[1])]
        else:
            res.append(prev)
            prev = itr

    if prev:
        res.append(prev)

    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
print(merge([[1, 4], [4, 5]]), [[1, 5]])
