# Flood Fill
# https://leetcode.com/problems/flood-fill/
# easy
#
# Tags: Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import deque
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int,
              newColor: int) -> List[List[int]]:
    oldColor = image[sr][sc]
    queue = deque([(sr, sc)])

    if oldColor == newColor:
        return image

    image[sr][sc] = newColor

    def inBounds(x, y):
        return x >= 0 and x < len(image) and y >= 0 and y < len(image[0])

    while queue:
        x, y = queue.popleft()
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = j + y
            if inBounds(ix, jy) and image[ix][jy] == oldColor:
                image[ix][jy] = newColor
                queue.append((ix, jy))

    return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
      [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
