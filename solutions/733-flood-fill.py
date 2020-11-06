# Flood Fill
# https://leetcode.com/problems/flood-fill/
# easy
#
# Tags: Amazon, Google, Microsoft
#
# Time:  O(E+V)
# Space: O(E+V)
#
# Solution:
# BFS

from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    n = len(image)
    m = len(image[0])
    color = image[sr][sc]
    image[sr][sc] = newColor
    queue = [(sr, sc)]

    while queue:
        x, y = queue.pop(0)

        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = j + y

            if ix >= 0 and ix < n and jy >= 0 and jy < m and image[ix][jy] == color and image[ix][jy] != newColor:
                queue.append((ix, jy))
                image[ix][jy] = newColor

    return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
