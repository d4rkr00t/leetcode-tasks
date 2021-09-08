# Array Nesting
# https://leetcode.com/problems/array-nesting/
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


def arrayNesting(nums: List[int]) -> int:
    visited = set()
    lens = [0] * len(nums)
    ans = 0

    def sim(pos):
        nonlocal ans
        if pos in visited:
            return lens[pos]

        visited.add(pos)
        next = nums[pos]
        res = 0

        if next > 0 and next < len(nums):
            res = sim(next)

        lens[pos] = res + 1
        ans = max(ans, lens[pos])

        return lens[pos]

    for i in range(len(nums)):
        sim(i)

    return ans


print(arrayNesting([5, 4, 0, 3, 1, 6, 2]), 4)
print(arrayNesting([0, 1, 2]), 1)
