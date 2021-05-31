# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# HashMap

from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    count = s = 0
    hm = {0: 1}

    for i in range(len(nums)):
        s += nums[i]
        if s - k in hm:
            count += hm[s - k]

        hm[s] = hm.get(s, 0)
        hm[s] += 1

    return count


print(subarraySum(nums=[1, 1, 1], k=2), 2)
print(subarraySum(nums=[1, 2, 3], k=3), 2)
