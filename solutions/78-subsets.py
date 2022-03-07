# Subsets
# https://leetcode.com/problems/subsets/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    ans = [[]]

    for n in nums:
        pos = 0
        end = len(ans)
        while pos < end:
            ans.append(ans[pos] + [n])
            pos += 1

    return ans


print(subsets([1, 2, 3]),
      [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []])

print(subsets([0]), [[], [0]])

# []
# [] [1]
# [] [1] [1, 2] [2]
# [] [1] [1, 2] [2] [3] [1,3] [1, 2, 3] [2 3]
