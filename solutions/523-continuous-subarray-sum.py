# Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(N)
# Space: O(N)
#
# Solution:
# Hash Table

from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    sums = {0: -1}
    sum = 0
    for i in range(len(nums)):
        n = nums[i]
        sum += n
        if k != 0:
            sum = sum % k

        if sum in sums:
            if i - sums[sum] > 1:
                return True
        else:
            sums[sum] = i

    return False

# 23 2 4 6 7
# sums = {5, 1}
# sum = 29
# i = 1


print(checkSubarraySum([23, 2, 4, 6, 7],  k=6), True)
