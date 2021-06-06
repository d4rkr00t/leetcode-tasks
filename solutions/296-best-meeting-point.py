# Best Meeting Point
# https://leetcode.com/problems/best-meeting-point/
# hard
#
# Tags: Google, Amazon
#
# Time:  O(m*n*k)
# Space: O(k)
#
# Solution:
# TBD

from typing import List


def minTotalDistance(grid: List[List[int]]) -> int:
    homes = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                homes.append((i, j))

    ans = float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                continue

            sum_dist = 0
            for (x1, y1) in homes:
                sum_dist += abs(x1 - i) + abs(y1 - j)

            ans = min(ans, sum_dist)

    return ans


print(minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 6)
