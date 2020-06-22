# Flood Fill
# https://leetcode.com/problems/flood-fill/
# easy
#
# Tags: Amazon, Google, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def floodFill(image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
    queue = [(sr,sc)]
    orig_color = image[sr][sc]
    if newColor == orig_color: return image

    while queue:
        i,j = queue.pop(0)
        image[i][j] = newColor

        for x,y in [(-1,0), (0,1), (1, 0), (0,-1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(image) and jy >= 0 and jy < len(image[0]) and image[ix][jy] == orig_color:
                queue.append((ix,jy))

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
