# Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(log(n))
# Space: O(1)
#
# Solution:
# Binary Search

def findPeakElement(nums: [int]) -> int:
    l = 0
    h = len(nums) - 1

    while l < h:
        mid = (l+h) // 2
        num = nums[mid]
        prev = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
        next = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")

        if prev < num > next:
            return mid

        if prev > num > next:
            h = mid - 1
        else:
            l = mid + 1

    return -1


print(findPeakElement([1,2,3,1]), 2)
print(findPeakElement([1,2,1,3,5,6,4,3]), 1, 5)

