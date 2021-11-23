# Maximum Number of Visible Points
# https://leetcode.com/problems/maximum-number-of-visible-points/
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
import math


def visiblePoints(points: List[List[int]], angle: int,
                  location: List[int]) -> int:
    array = []
    nloc = 0
    for p in points:
        if p == location:
            nloc += 1
        else:
            array.append(
                math.degrees(math.atan2(p[1] - location[1],
                                        p[0] - location[0])))
    array.sort()
    angles = array + [a + 360 for a in array]
    left, maxm = 0, 0
    for right, a in enumerate(angles):
        if a - angles[left] > angle:
            left += 1
        maxm = max(right - left + 1, maxm)

    return maxm + nloc


print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]),
    3)

print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]],
                  angle=90,
                  location=[1, 1]), 4)

print(visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]), 1)
