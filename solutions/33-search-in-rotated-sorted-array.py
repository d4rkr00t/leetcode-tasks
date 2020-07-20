# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def search(nums: [int], target: int) -> int:
    if not nums:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    # 1. find rotation
    lo = 0
    hi = len(nums) - 1
    pivot = (hi+lo) // 2

    while lo <= hi:
        pivot = (hi+lo) // 2
        if nums[pivot] > nums[pivot+1]:
            pivot += 1
            break
        else:
            if nums[pivot] < nums[lo]:
                hi = pivot - 1
            else:
                lo = pivot + 1

    # 2. bs
    def bs(start, end):
        mid = (end+start) // 2

        if start > end:
            return -1

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return bs(mid+1, end)

        return bs(start, mid-1)

    return max(bs(0, pivot-1), bs(pivot, len(nums)-1))


print(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
print(search([4, 5, 6, 7, 0, 1, 2], 3), -1)

# 2, 4, 5, 6, 7, 0, 1
#
