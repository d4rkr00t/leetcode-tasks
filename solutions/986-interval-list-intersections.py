# Interval  Intersections
# https://leetcode.com/problems/interval-list-intersections/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def intervalIntersection(firstList: List[List[int]],
                         secondList: List[List[int]]) -> List[List[int]]:
    ans = []
    fpos = 0
    spos = 0

    while fpos < len(firstList) and spos < len(secondList):
        fint = firstList[fpos]
        sint = secondList[spos]

        if fint[0] <= sint[1] and fint[1] >= sint[0]:
            ans.append([max(fint[0], sint[0]), min(fint[1], sint[1])])

        if fint[1] >= sint[1]:
            spos += 1
        else:
            fpos += 1

    return ans


print(
    intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                         [[1, 5], [8, 12], [15, 24], [25, 26]]),
    [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])
