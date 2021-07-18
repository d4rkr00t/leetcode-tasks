# Add Minimum Number of Rungs
# https://leetcode.com/contest/weekly-contest-250/problems/add-minimum-number-of-rungs/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def addRungs(rungs: List[int], dist: int) -> int:
    ans = 0
    cur = 0

    for r in rungs:
        diff = r - cur
        if diff > dist:
            q, c = divmod(diff, dist)
            ans += q
            if c == 0:
                ans -= 1

        cur = r

    return ans


# diff = 3,
print(addRungs(rungs=[15, 26, 29], dist=4), 5)
print(addRungs(rungs=[3], dist=1), 2)
print(addRungs(rungs=[3], dist=2), 1)
print(addRungs(rungs=[1, 3, 5, 10], dist=2), 2)
print(addRungs(rungs=[3, 6, 8, 10], dist=3), 0)
print(addRungs(rungs=[3, 4, 6, 7], dist=2), 1)
print(addRungs(rungs=[5], dist=10), 0)
