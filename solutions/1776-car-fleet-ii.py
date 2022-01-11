# Car Fleet II
# https://leetcode.com/problems/car-fleet-ii/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def getCollisionTimes(cars: List[List[int]]) -> List[float]:
    n = len(cars)
    answer = [-1.0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack:
            if cars[i][1] <= cars[stack[-1]][1] or (
                (cars[stack[-1]][0] - cars[i][0]) /
                (cars[i][1] - cars[stack[-1]][1])
            ) > answer[stack[-1]] and answer[stack[-1]] > 0:
                stack.pop()
            else:
                answer[i] = (cars[stack[-1]][0] -
                             cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
                break

        stack.append(i)

    return answer


print(getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]),
      [1.00000, -1.00000, 3.00000, -1.00000])
print(getCollisionTimes([[3, 4], [5, 4], [6, 3], [9, 1]]),
      [2.00000, 1.00000, 1.50000, -1.00000])

# [[1, 2], [2, 1], [4, 3], [7, 2]]
# [[1, 2]] [2, 1]
