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

import collections


def permuteUnique(nums: [int]) -> [[int]]:
    pmt = []
    counter = collections.Counter(nums)

    def backtrack(res):
        if len(nums) == len(res):
            pmt.append([] + res)
            return

        for key in counter.keys():
            if counter[key] == 0:
                continue

            counter[key] -= 1
            res.append(key)
            backtrack(res)
            counter[key] += 1
            res.pop()

    backtrack([])

    return pmt


print(permuteUnique([1, 1, 2]), [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
])
