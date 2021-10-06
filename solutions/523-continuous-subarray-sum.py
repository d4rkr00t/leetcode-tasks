# Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

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


# print(checkSubarraySum([23, 2, 4, 6, 7], k=6), True)
# print(checkSubarraySum([23, 2, 6, 4, 7], k=13), False)
print(checkSubarraySum([23, 2, 4, 6, 6], k=7), True)

#        23  2  4  6  6
#    n = 6
#    s = 0
# sums = {0:-1,2:0, 4:1, 1:2}
#
