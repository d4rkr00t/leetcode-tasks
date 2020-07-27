# Two Sum
# https://leetcode.com/problems/two-sum/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def twoSum(nums: [int], target: int) -> [int]:
    table = {}

    for i, n in enumerate(nums):
        if n in table:
            return [table[n], i]
        else:
            table[target-n] = i

    return []


print(twoSum(nums=[2, 7, 11, 15], target=9), [0, 1])
