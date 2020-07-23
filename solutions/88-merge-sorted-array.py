# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# easy
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    nums1[:p2 + 1] = nums2[:p2+1]

    return nums1


print(merge([1, 2, 3, 0, 0, 0, 0, 0], 3, [
      1, 2, 2, 5, 6], 5), [1, 2, 2, 3, 5, 6])

# [1, 2, 3, 0, 0, 0, 0, 0]
# p1 = 2
# p2 = 4
# p = 7

# [1, 2, 3, 0, 0, 0, 0, 6]
# p1 = 2
# p2 = 3
# p = 6

# [1, 2, 3, 0, 0, 0, 5, 6]
# p1 = 2
# p2 = 2
# p = 5

# [1, 2, 3, 0, 0, 3, 5, 6]
# p1 = 1
# p2 = 2
# p = 4

# [1, 2, 3, 0, 2, 3, 5, 6]
# p1 = 1
# p2 = 1
# p = 3

# [1, 1, 2, 2, 2, 3, 5, 6]
# p1 = 1
# p2 = 0
# p = 2
