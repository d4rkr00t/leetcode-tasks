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
    prev = lower - 1
    ranges = []

    def process(prev, cur):
        dist = cur - prev

        if dist <= 1:
            None
        elif dist == 2:
            ranges.append(str((cur + prev) // 2))
        else:
            ranges.append(str(prev + 1) + "->" + str(cur - 1))

    for n in nums:
        process(prev, n)
        prev = n

    process(prev, upper + 1)

    return ranges


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99),
      ["2", "4->49", "51->74", "76->99"])

# -1
# 1
# 1 + 1 = 2
