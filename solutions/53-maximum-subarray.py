# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# easy
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


from typing import List


def maxSubArray(nums: List[int]) -> int:
    sum = 0
    ans = float("-inf")

    for i in range(len(nums)):
        sum += nums[i]

        if sum < nums[i]:
            sum = nums[i]

        ans = max(sum, ans)

    return ans


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
