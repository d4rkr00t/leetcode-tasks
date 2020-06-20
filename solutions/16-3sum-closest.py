# 3Sum Closest
# https://leetcode.com/problems/3sum-closest/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time: O(n^2)
# Space: O(n)
#
# Solution:
# TBD

def threeSumClosest(nums: [int], target: int) -> int:
    closest = float("inf")
    nums.sort()

    for i in range(len(nums)):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(s - target) < abs(closest - target):
                closest = s

            if s < target:
                lo += 1
            else:
                hi -= 1

        if closest - target == 0:
            break

    return closest


print(threeSumClosest(nums = [-1,2,1,-4], target = 1), 2)
