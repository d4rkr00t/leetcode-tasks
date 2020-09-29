# Missing Ranges
# https://leetcode.com/problems/missing-ranges/
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


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    nums.insert(0, lower - 1)
    nums.append(upper + 1)

    prev = nums[0]
    ans = []
    for n in nums[1:]:
        if n - prev == 2:
            ans.append(str(n-1))
        elif n - prev > 2:
            ans.append(str(prev + 1) + "->" + str(n-1))

        prev = n

    return ans


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99),
      ["2", "4->49", "51->74", "76->99"])
