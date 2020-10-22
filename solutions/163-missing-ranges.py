# Missing Ranges
# https://leetcode.com/problems/missing-ranges/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Linear scan

from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    nums = [lower-1] + nums + [upper + 1]
    cur = nums[0]
    ans = []
    for i in range(1, len(nums)):
        next = nums[i]
        if next - cur == 2:
            ans.append(str((next+cur) // 2))
        elif next - cur > 2:
            ans.append(str(cur + 1) + "->" + str(next-1))

        cur = next

    return ans


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99),
      ["2", "4->49", "51->74", "76->99"])
