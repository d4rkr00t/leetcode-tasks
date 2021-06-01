# Permutations II
# https://leetcode.com/problems/permutations-ii/
# medium
#
# Tags: Amazon
#
# Time:  O(n!/(n-k)!) where n candidates
# Space: O(n)
#
# Solution:
# TBD

from typing import List
import collections


def permuteUnique(nums: List[int]) -> List[List[int]]:
    ans = []
    counter = collections.Counter(nums)

    def permute(cur):
        if len(cur) == len(nums):
            ans.append([] + cur)
            return

        for k in counter.keys():
            if counter[k] <= 0:
                continue

            counter[k] -= 1
            cur.append(k)
            permute(cur)
            cur.pop()
            counter[k] += 1

    permute([])

    return ans


print(permuteUnique([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
