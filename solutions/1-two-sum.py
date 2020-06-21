# Two Sum
# https://leetcode.com/problems/two-sum/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def twoSum(nums: [int], target: int) -> [int]:
    ht = {}
    for i,n in enumerate(nums):
        if target - n in ht:
            return [ht[target-n], i]

        ht[n] = i

    return []

print(twoSum(nums = [2, 7, 11, 15], target = 9), [0,1])
