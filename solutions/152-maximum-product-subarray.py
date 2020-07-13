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
    global_max = max_p = min_p = nums[0]

    for n in nums[1:]:
        cur_min = min(min_p * n, max_p * n, n)
        cur_max = max(min_p * n, max_p * n, n)
        global_max = max(global_max, cur_max)
        max_p = cur_max
        min_p = cur_min

    return global_max


print(maxProduct([2, 3, -2, 4]), 6)
print(maxProduct([2, 3, -2, 4, -1]), 48)
print(maxProduct([-2, 0, -1]), 0)

#      2 3 -2    4 -1
# min: 2 6 -12 -48 -48
# max: 2 6   6   6  48

#      2 3 -2    4
# min: 2 6 -12 -48
# max: 2 6   6   6

#      -2 0 -1
# min: -2 0 -1
# max: -2 0  0
