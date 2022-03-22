# Permutations
# https://leetcode.com/problems/permutations/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(cur, available):
        if len(cur) == len(nums):
            ans.append([] + cur)
            return

        for i in range(len(available)):
            cur.append(available[i])
            backtrack(cur, available[:i] + available[i + 1:])
            cur.pop()

    backtrack([], nums)

    return ans


print(permute([1, 2, 3]),
      [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
