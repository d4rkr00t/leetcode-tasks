# Car Fleet
# https://leetcode.com/problems/car-fleet/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    res = len(position)
    finishing = [(target - p) / s for p, s in sorted(
        zip(position, speed), key=lambda k: k[0], reverse=True)]
    mxSpeed = finishing[0]

    for i in range(1, len(finishing)):
        if finishing[i] <= mxSpeed:
            res -= 1
        else:
            mxSpeed = finishing[i]

    return res


print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]), 3)
print(carFleet(target=10, position=[3], speed=[3]), 1)
print(carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]), 1)

# a = 0
# p = [10, 8, 0, 5, 3]
# s = [2,  4, 1, 1, 3]

# a = 0
# p = [12, 1, 6]
# s = [2,  1, 1]

# a = 1
# p = [1, 6]
# s = [1, 1]
