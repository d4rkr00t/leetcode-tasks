# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(n*log(n))
# Space: O(1)
#
# Solution:
# Binary Search

def searchRange(nums: [int], target: int) -> [int]:
    def bs(nums, target, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return bs(nums, target, mid + 1, end)

        return bs(nums, target, start, mid - 1)

    start = bs(nums, target, 0, len(nums) - 1)

    if start == -1:
        return [-1, -1]

    left = right = end = start

    while left != -1:
        left = bs(nums, target, 0, left-1)
        if left > -1:
            start = left

    while right != -1:
        right = bs(nums, target, right+1, len(nums)-1)
        if right > -1:
            end = right

    return [start, end]

print(searchRange(nums = [1], target = 1), [0,0])
print(searchRange(nums = [2,2], target = 2), [0,1])
print(searchRange(nums = [5,7,7,8,8,10], target = 8), [3,4])
print(searchRange(nums = [5,7,7,8,8,10], target = 6), [-1,-1])
