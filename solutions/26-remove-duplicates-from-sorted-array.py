# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# easy
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def removeDuplicates(nums: [int]) -> int:
    if len(nums) < 2:
        return len(nums)

    p1 = 0

    for i in range(1, len(nums)):
        if nums[p1] == nums[i]:
            continue

        nums[p1+1], nums[i] = nums[i], nums[p1+1]
        p1 += 1

    return p1+1


print(removeDuplicates([1, 1, 2]), 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
