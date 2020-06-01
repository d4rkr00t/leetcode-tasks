# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# medium
#
# Tags: Amazon, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

def maxArea(height: [int]) -> int:
    s = 0
    e = len(height) - 1
    m = 0

    while s < e:
        y = min(height[s], height[e])
        x = e-s
        m = max(m, y*x)

        if height[e] <= height[s]:
            e -= 1
        else:
            s += 1

    return m

print(maxArea([1,8,6,2,5,4,8,3,7]), 49)
