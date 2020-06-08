# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def maxProduct(nums: [int]) -> int:
    max_pro = min_pro = ans = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        temp_max = max_pro
        max_pro = max(n, n * max_pro, n * min_pro)
        min_pro = min(n, n * temp_max, n * min_pro)
        ans = max(max_pro, ans)

    return ans


print(maxProduct([2,3,-2,4,-1]), 48)
print(maxProduct([2,3,-2,4]), 6)
print(maxProduct([-2,0,-1]), 0)

# 2 * 3 * -2 * 4 * -1
#            4

# 2 * 3 * -2 * 4 * -1
