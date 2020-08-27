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


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    o_c = image[sr][sc]
    queue = [(sr, sc)]
    image[sr][sc] = newColor
    visited = set((sr, sc))

    while queue:
        x, y = queue.pop(0)

        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xi = x + i
            yj = y + j

            if xi >= 0 and yj >= 0 and xi < len(image) and yj < len(image[0]) and image[xi][yj] == o_c and (xi, yj) not in visited:
                image[xi][yj] = newColor
                queue.append((xi, yj))
                visited.add((xi, yj))

    return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
