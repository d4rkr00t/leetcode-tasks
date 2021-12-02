# Max Value of Equation
# https://leetcode.com/problems/max-value-of-equation/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
from collections import deque


def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    ans = float("-inf")
    queue = deque()
    for x, y in points:
        while queue and x - queue[0][0] > k:
            queue.popleft()
        if queue:
            ans = max(ans, queue[0][1] + y + x - queue[0][0])
        while queue and queue[-1][1] + x - queue[-1][0] <= y:
            queue.pop()
        queue.append([x, y])
    return ans


print(findMaxValueOfEquation(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1),
      4)
print(findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3), 3)

# yi + yj + |xi - xj|
#
# [1, 3], [2, 0], [5, 10], [6, -10]
# [
#  [5,5,2],
#  [2,1,0],
#  [-2,2,1],
#  [-16,6,3],
# ]
#
# [5,5,2] [1,3] 5-1 = 4
# [
#  [2,1,0],
#  [-2,2,1],
#  [-16,6,3],
# ]
#
