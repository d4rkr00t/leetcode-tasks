# 3Sum
# https://leetcode.com/problems/3sum/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    ans = set()
    nums.sort()
    for i, ni in enumerate(nums):
        table = {}
        for j in range(i + 1, len(nums)):
            nj = nums[j]
            summ = 0 - (ni + nj)
            if summ in table:
                ans.add(tuple(sorted([ni, summ, nj])))

            table[nj] = j

    return list(ans)


print(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

# -1, 0, 1, 2, -1, -4
# -4, -1, -1, 0, 1, 2
#      i            j
# summ = 1
# table = {0}
