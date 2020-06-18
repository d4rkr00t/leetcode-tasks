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
    hm = {0: -1}

    s = 0
    for i in range(len(nums)):
        s += nums[i]

        if k != 0:
            s = s % k

        if s in hm:
            if i - hm[s] > 1:
                return True
        else:
            hm[s] = i

print(checkSubarraySum([23, 2, 4, 6],  k=6), True)
