# 3Sum
# https://leetcode.com/problems/3sum/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# TBD

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = set()
    dups = set()
    seen = {}

    for i, ival in enumerate(nums):
        if ival not in dups:
            dups.add(ival)
            for j, jval in enumerate(nums[i + 1:]):
                compl = -ival - jval
                if compl in seen and seen[compl] == i:
                    res.add(tuple(sorted([ival, jval, compl])))
                seen[jval] = i

    return list(res)


print(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

# -1
# 0 - 1 = -1
