# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# hard
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def trap(height: [int]) -> int:
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    ans = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                ans += left_max - height[left]

            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                ans += right_max - height[right]

            right -= 1

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

#               3
#       2 # # # 3 2 # 2
# _ 1 # 2 1 # 1 3 2 1 2 1
# |                     |
