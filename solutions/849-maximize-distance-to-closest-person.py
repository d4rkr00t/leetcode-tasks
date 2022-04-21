# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# medium
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    prev = None
    ans = 0

    for i, p in enumerate(seats):
        if p == 0 and i != len(seats) - 1:
            continue

        if prev == None:
            ans = max(ans, i)
        elif i == len(seats) - 1 and p == 0:
            ans = max(ans, i - prev)
        else:
            ans = max(ans, (i - prev) // 2)
        prev = i
    return ans


print(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)
print(maxDistToClosest([1, 0, 0, 0]), 3)
print(maxDistToClosest([0, 0, 0, 1]), 3)
