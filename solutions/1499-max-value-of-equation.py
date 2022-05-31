# Max Value of Equation
# https://leetcode.com/problems/max-value-of-equation/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import deque
from typing import List

# yi + yj + |xi - xj|
# |xi - xj| <= k


def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    ans = float("-inf")
    queue = deque()

    for x, y in points:
        while queue and x - queue[0][0] > k:
            queue.popleft()

        if queue:
            ans = max(ans, y + queue[0][1] + x - queue[0][0])

        while queue and queue[-1][1] + x - queue[-1][0] < y:
            queue.pop()

        queue.append((x, y))

    return ans


print(findMaxValueOfEquation(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1),
      4)
print(findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3), 3)
