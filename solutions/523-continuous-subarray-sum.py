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


print(checkSubarraySum([23, 2, 4, 6, 7], k=13), True)

# 23  2  4  6  7
# 23 25 29 35 42
