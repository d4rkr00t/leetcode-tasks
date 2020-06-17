# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(log(N))
# Space: O(1)
#
# Solution:
# Binary Search

def search(nums: [int], target: int) -> int:
    if not nums:
        return -1

    def find_rotation(nums, start, end):
        if start > end: return 0

        mid = (end + start) // 2

        if mid + 1 >= len(nums):
            return 0

        if nums[mid] > nums[mid + 1]:
            return mid

        return max(
            find_rotation(nums, start, mid - 1),
            find_rotation(nums, mid + 1, end),
        )

    def bs(nums, start, end, target):
        if start > end: return -1

        mid = (end + start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return bs(nums, mid + 1, end, target)
        else:
            return bs(nums, start, mid - 1, target)

    rotation = find_rotation(nums, 0, len(nums)-1)

    left = bs(nums, 0, rotation, target)
    right = bs(nums, rotation + 1, len(nums) - 1, target)

    return -1 if left == -1 and right == -1 else max(left, right)


# print(search([4,5,6,7,0,1,2], 0), 4)
# print(search([4,5,6,7,0,1,2], 3), -1)
# print(search([3,1], 1), 1)
print(search([2,3,4,5,1], 1), 4)
