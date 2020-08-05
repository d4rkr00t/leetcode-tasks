# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def b_search(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        n = nums[mid]

        if n == target:
            return mid
        if n < target:
            return b_search(mid + 1, end)

        return b_search(start, mid-1)

    pos = b_search(0, len(nums) - 1)

    if pos == -1:
        return [-1, -1]

    left = right = pos

    while left:
        next_left = b_search(0, left-1)
        if next_left == -1:
            break

        left = next_left

    while right < len(nums) - 1:
        next_right = b_search(right+1, len(nums) - 1)
        if next_right == -1:
            break

        right = next_right

    return [left, right]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4])
print(searchRange(nums=[5, 7, 7, 8, 8, 8, 8, 8, 10], target=8), [3, 7])
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1])
