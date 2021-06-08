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
    count = s = 0
    hm = {0: 1}

    for n in nums:
        s += n
        if s - k in hm:
            count += hm[s - k]

        hm[s] = hm.get(s, 0) + 1

    return count


# print(subarraySum(nums=[1, 1, 1], k=2), 2)

# count = 4
# hm = {0: 1, 1: 2, 2: 2, 3:1}
# s = 3
# n = 1
print(subarraySum(nums=[1, 1, -1, 1, 1], k=2), 4)
