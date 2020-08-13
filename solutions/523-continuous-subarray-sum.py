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
    sums = {}
    s = 0
    for i, n in enumerate(nums):
        s += n
        if s % k in sums and i - sums[s % k] >= 2:
            return True

        sums[s % k] = i

    return False


print(checkSubarraySum([23, 2, 4, 6, 7],  k=6), True)

# s = 29
# s%= 5
# { 5: 0, 1: 25,  }
