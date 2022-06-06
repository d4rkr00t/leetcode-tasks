# Missing Ranges
# https://leetcode.com/problems/missing-ranges/
# easy
#
# Tags: Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    nums.append(upper + 1)
    prev = lower - 1
    missing = []

    for n in nums:
        if n - prev == 2:
            missing.append(str(n - 1))
        elif n - prev > 2:
            missing.append(str(prev + 1) + "->" + str(n - 1))

        prev = n

    return missing


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99),
      ["2", "4->49", "51->74", "76->99"])

print(findMissingRanges([-1], -1, -1), [])
