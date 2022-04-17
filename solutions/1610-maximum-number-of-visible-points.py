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

import math
from typing import List


def visiblePoints(points: List[List[int]], angle: int,
                  location: List[int]) -> int:
    nloc = lo = ans = 0
    angles = []

    for p in points:
        if p == location:
            nloc += 1
        else:
            angles.append(
                math.degrees(math.atan2(p[1] - location[1],
                                        p[0] - location[0])))
    angles.sort()
    angles += [a + 360 for a in angles]

    for hi, a in enumerate(angles):
        if a - angles[lo] <= angle:
            ans = max(hi - lo + 1, ans)
        else:
            lo += 1

    return ans + nloc


print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]),
    3)

print(
    visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]],
                  angle=90,
                  location=[1, 1]), 4)

print(visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]), 1)

#       |
#       |
#       |
# ––––– x ––––––––
#       |
#       |
