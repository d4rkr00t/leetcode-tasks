# Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def findPeakElement(nums: [int]) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        prev = nums[mid-1] if mid > 0 else float("-inf")
        next = nums[mid+1] if mid+1 < len(nums) else float("-inf")

        if prev < nums[mid] > next:
            return mid

        if prev < nums[mid] < next:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


print(findPeakElement([1, 2, 3, 1]), 2)
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]), 1, 5)
print(findPeakElement([1]), 0)
print(findPeakElement([1, 2]), 1)
