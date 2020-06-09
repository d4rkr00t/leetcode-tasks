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
    i = 0

    for j in range(1, len(nums)):
        if (nums[i] != nums[j]):
            i += 1
            nums[i] = nums[j]

    return i + 1

print(removeDuplicates([1,1,2]), 2)
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)
