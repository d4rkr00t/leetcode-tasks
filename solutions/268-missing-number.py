# Missing Number
# https://leetcode.com/problems/missing-number/
# easy
#
# Tags: Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def missingNumber(nums: [int]) -> int:
    missing = len(nums)

    for i, n in enumerate(nums):
        missing ^= i ^ n

    return missing


print(missingNumber([3, 0, 1]), 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
