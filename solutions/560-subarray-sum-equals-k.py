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
    prev = {0: 1}
    ans = sm = 0

    for n in nums:
        sm += n
        if sm - k in prev:
            ans += prev[sm - k]
        prev[sm] = prev.get(sm, 0) + 1

    return ans


print(subarraySum(nums=[1, 1, 1, 1], k=2), 3)
print(subarraySum(nums=[1, 2, 3], k=3), 2)
print(subarraySum(nums=[1, 0, 1, 1], k=2), 3)
