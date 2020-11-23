# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(log(n))
# Space: O(h)
#
# Solution:
# TBD

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def bsearch(s, e, t):
        if s > e:
            return -1

        mid = (s + e) // 2

        if nums[mid] == t:
            return mid

        if nums[mid] > t:
            return bsearch(s, mid - 1, t)

        return bsearch(mid + 1, e, t)

    n = len(nums) - 1
    item = bsearch(0, n, target)

    if item == -1:
        return [-1, -1]

    right = item
    while True:
        tmp = bsearch(right + 1, n, target)
        if tmp == -1:
            break
        right = tmp

    left = item
    while True:
        tmp = bsearch(0, left - 1, target)
        if tmp == -1:
            break
        left = tmp

    return [left, right]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4])
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1])
