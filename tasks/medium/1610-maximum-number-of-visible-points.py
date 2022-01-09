# Maximum Number of Visible Points
# https://leetcode.com/problems/maximum-number-of-visible-points/
# hard
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def visiblePoints(points: List[List[int]], angle: int,
                  location: List[int]) -> int:
    pass


print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]),
    3)

print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]],
                  angle=90,
                  location=[1, 1]), 4)

print(visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]), 1)
