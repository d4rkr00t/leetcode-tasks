# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    next_dir = {}
    next_dir[0, 1] = (1, 0)
    next_dir[1, 0] = (0, -1)
    next_dir[0, -1] = (-1, 0)
    next_dir[-1, 0] = (0, 1)
    dir = (0, 1)
    x = y = 0
    ans = []
    n = len(matrix) - 1
    m = len(matrix[0]) - 1

    while matrix[x][y] != "#":
        ans.append(matrix[x][y])
        matrix[x][y] = "#"
        nx = max(0, min(x + dir[0], n))
        ny = max(0, min(y + dir[1], m))

        if matrix[nx][ny] == "#":
            dir = next_dir[dir]
            x = max(0, min(x + dir[0], n))
            y = max(0, min(y + dir[1], m))
        else:
            x = nx
            y = ny

    return ans


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
      [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
      [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
