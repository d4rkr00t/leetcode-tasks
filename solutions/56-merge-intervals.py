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
    res = []
    cur = None

    for x1, y1 in sorted(intervals):
        if not cur:
            cur = (x1, y1)
            continue

        if cur[1] >= x1 and cur[0] <= y1:
            cur = (min(x1, cur[0]), max(y1, cur[1]))
        else:
            res.append(cur)
            cur = (x1, y1)

    if cur:
        res.append(cur)

    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
print(merge([[1, 4], [4, 5]]), [[1, 5]])
