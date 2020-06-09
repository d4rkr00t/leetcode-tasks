# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# easy
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers


def maxSubArray(nums: [int]) -> int:
    if not nums: return 0
    sum = 0
    ans = float("-inf")

    for i,n in enumerate(nums):
        sum = max(n, sum+n)
        ans = max(sum, ans)

    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
print(maxSubArray([-2,3,1,3]), 7)

