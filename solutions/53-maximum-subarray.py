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


def maxSubArray(nums: [int]) -> int:
    if not nums:
        return 0

    sum = 0
    ans = float("-inf")

    for n in nums:
        sum = max(n, sum + n)
        ans = max(ans, sum)

    return ans


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
