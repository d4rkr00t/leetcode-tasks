# Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    pass


print(
    closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0],
                  [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0]]), 2)

print(closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]), 1)

print(
    closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1]]), 2)
