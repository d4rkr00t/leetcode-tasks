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
    res = []
    found = set()
    dups = set()
    seen = {}
    for i, n1 in enumerate(nums):
        if n1 not in dups:
            dups.add(n1)

            for n2 in nums[i+1:]:
                c = -n1 - n2
                if c in seen and seen[c] == i:
                    min_val = min([n1, n2, c])
                    max_val = max([n1, n2, c])

                    if (min_val, max_val) not in found:
                        found.add((min_val, max_val))
                        res.append([n1, n2, c])

                seen[n2] = i

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]), [
    [-1, 0, 1],
    [-1, -1, 2]
])

# -1 0 1 2 -1 -4
#
