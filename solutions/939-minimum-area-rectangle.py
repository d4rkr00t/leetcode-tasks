# Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/
# medium
#
# Tags: Google, Facebook
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# TBD

from typing import List
import collections


def minAreaRect(points: List[List[int]]) -> int:
    seen = set()
    ans = float("inf")

    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        seen.add((x1, y1))

    return ans if ans < float("inf") else 0


print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)
print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]), 2)

# (1,1)  (1,3)
#    (2, 2)
# (3,1)  (3,3)

# (1, 1)  (1, 3)
#
# (3, 1)  (3, 3)
#
# (4, 1)  (4, 3)

# rows = {1: [(1 ,1), (1, 3)], 2: [(2, 2)], 3: [(3, 1), (3, 3)]}
# cols = {1: [(1, 1), (3, 1)], 2: [(2, 2)], 3: [(1, 3), (3, 3)]}

# (r,c) = (1,1)
# rows[r] = [(1, 3)]
# cols[c] = [(3, 1)]
#
