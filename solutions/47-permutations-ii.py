# Permutations II
# https://leetcode.com/problems/permutations-ii/
# medium
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import collections


def permuteUnique(nums: List[int]) -> List[List[int]]:
    ans = []
    counter = collections.Counter(nums)

    def permute(cur):
        nonlocal ans

        if len(cur) == len(nums):
            ans.append([] + cur)
            return

        for key in counter.keys():
            if counter[key] <= 0:
                continue

            counter[key] -= 1
            cur.append(key)
            permute(cur)
            cur.pop()
            counter[key] += 1

    permute([])

    return ans


print(permuteUnique([1, 1, 2]), [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
])
