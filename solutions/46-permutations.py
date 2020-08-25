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

    def backtrack(i):
        if i == len(nums):
            ans.append(nums[:])

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(i+1)
            nums[i], nums[j] = nums[j], nums[i]

    backtrack(0)
    return ans


print(permute([1, 2, 3]), [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
])

# [1], [2], [3]
# [1,2], [1,3] [2,1], [2,3], [3,1] [3,2]
# [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
