# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# medium
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    lo = 0
    md = 0

    for hi in range(len(seats)):
        if seats[hi] != 1 and hi != len(seats) - 1:
            continue

        if lo == 0 and seats[lo] == 0:
            md = max(md, hi)
        elif hi == len(seats) - 1 and seats[hi] == 0:
            md = max(md, hi - lo)
        else:
            md = max(md, (hi - lo) // 2)

        lo = hi

    return md


print(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)
print(maxDistToClosest([1, 0, 0, 0]), 3)
print(maxDistToClosest([0, 0, 0, 1]), 3)
