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

from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int,
              newColor: int) -> List[List[int]]:
    srcColor = image[sr][sc]
    if srcColor == newColor:
        return image

    queue = [(sr, sc)]
    image[sr][sc] = newColor

    def inboounds(x, y):
        return x >= 0 and x < len(image) and y >= 0 and y < len(image[0])

    while queue:
        x, y = queue.pop(0)
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = j + y

            if inboounds(ix, jy) and image[ix][jy] == srcColor:
                queue.append((ix, jy))
                image[ix][jy] = newColor

    return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
      [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
