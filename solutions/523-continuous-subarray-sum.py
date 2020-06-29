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

def checkSubarraySum(nums: [int], k: int) -> bool:
    table = { 0: -1 }

    s = 0
    for i,n in enumerate(nums):
        s += n
        if k != 0:
            s = s % k
        if s in table:
            if i - table[s] > 1:
                return True
        else:
            table[s] = i

    return False

print(checkSubarraySum([23, 2, 4, 6, 7],  k=6), True)
