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

def floodFill(image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
    color = image[sr][sc]

    queue = [(sr,sc)]
    image[sr][sc] = newColor
    while queue:
        r,c = queue.pop(0)

        for x,y in [(-1,0), (0,1), (1,0), (0, -1)]:
            rx = x + r
            cy = c + y

            if rx >= 0 and rx < len(image) and cy >= 0 and cy < len(image[0]) and image[rx][cy] == color:
                image[rx][cy] = newColor
                queue.append((rx,cy))

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
