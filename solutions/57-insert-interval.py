# Insert Interval
# https://leetcode.com/problems/insert-interval/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    cur = newInterval
    for i in range(len(intervals)):
        intr = intervals[i]
        if not cur:
            res.append(intr)
            continue

        if cur[0] <= intr[1] and cur[1] >= intr[0]:
            cur = [min(cur[0], intr[0]), max(cur[1], intr[1])]
        else:
            if cur[1] < intr[0]:
                res.append(cur)
                cur = None

            res.append(intr)

    if cur:
        res.append(cur)

    return res


print(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
             [4, 8]), [[1, 2], [3, 10], [12, 16]])
