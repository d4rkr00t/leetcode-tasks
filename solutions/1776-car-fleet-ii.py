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
    stack = []
    ans = [-1.0] * len(cars)

    for i in range(len(cars) - 1, -1, -1):
        car = cars[i]

        while stack:
            cur = stack[-1]
            nextCar = cars[cur]

            if car[1] <= nextCar[1] or (nextCar[0] - car[0]) / (
                    car[1] - nextCar[1]) > ans[cur] and ans[cur] > 0:
                stack.pop()
            else:
                ans[i] = (nextCar[0] - car[0]) / (car[1] - nextCar[1])
                break

        stack.append(i)

    return ans


# print(getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]),
#       [1.00000, -1.00000, 3.00000, -1.00000])
print(getCollisionTimes([[3, 4], [5, 4], [6, 3], [9, 1]]),
      [2.00000, 1.00000, 1.50000, -1.00000])

# (9 - 6) / (3 - 1) = 1.5
# [[6,3]]
