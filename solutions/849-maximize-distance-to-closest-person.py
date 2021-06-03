# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# medium
#
# Tags: Amazon, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    prev_idx = -1
    ans = 0

    for i, s in enumerate(seats):
        if s == 1:
            if prev_idx == -1:
                ans = max(ans, i)
            else:
                ans = max(((i + prev_idx) // 2) - prev_idx, ans)
            prev_idx = i

        if i == len(seats) - 1 and s == 0:
            ans = max(ans, len(seats) - prev_idx - 1)

    return ans


# prev_idx = 4
# ans = 2
# i = 6, s = 1
print(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)
print(maxDistToClosest([1, 0, 0, 0]), 3)
print(maxDistToClosest([0, 0, 0, 1]), 3)
print(maxDistToClosest([0, 0, 1, 0]), 2)
print(maxDistToClosest([0, 1]), 1)
print(maxDistToClosest([1, 0]), 1)

# 1 0 0 0 1 0 1
# ^       ^
