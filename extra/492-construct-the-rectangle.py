# Construct the Rectangle
# https://leetcode.com/problems/construct-the-rectangle/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
from math import sqrt, ceil


def constructRectangle(area: int) -> List[int]:
    start = ceil(sqrt(area))

    while area % start > 0 and start < area:
        start += 1

    if area % start == 0:
        return [start, area // start]

    return None


print(constructRectangle(4), [2, 2])
print(constructRectangle(37), [37, 1])
print(constructRectangle(122122), [427, 286])
