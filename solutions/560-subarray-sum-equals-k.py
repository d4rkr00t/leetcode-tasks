# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    count = sum = 0
    hm = {0: 1}

    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in hm:
            count += hm[sum - k]

        hm[sum] = hm.get(sum, 0)
        hm[sum] += 1

    return count


print(subarraySum(nums=[1, 1, 1], k=2), 2)

# 0 1 2 3
#
