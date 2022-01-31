# Insert Interval
# https://leetcode.com/problems/insert-interval/
# medium
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from bisect import bisect
from typing import List


def insert(intervals: List[List[int]],
           newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]

    start = newInterval[0]
    end = newInterval[1]

    left = bisect.bisect_left(intervals, start, key=lambda i: i[1])
    right = bisect.bisect(intervals, end, key=lambda i: i[0])

    if left < len(intervals):
        start = min(intervals[left][0], start)

    if intervals[right - 1][0] <= end:
        end = max(intervals[right - 1][1], end)

    intervals[left:right] = [[start, end]]

    return intervals


print(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
      [[1, 2], [3, 10], [12, 16]])
