# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# hard
#
# Tags: Microsoft, Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    n = len(nums1)
    m = len(nums2)
    if n > m:
        return findMedianSortedArrays(nums2, nums1)

    imin = 0
    imax = n
    half_len = (n + m + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < n and nums2[j-1] > nums1[i]:
            imin = i+1
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums2[j-1], nums1[i-1])

            if (n+m) % 2 == 1:
                return max_of_left

            if i == n:
                min_of_right = nums2[j]
            elif j == m:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums2[j], nums1[i])

            return (min_of_right + max_of_left) / 2

    return -1


print(findMedianSortedArrays([1, 3], [2]), 2.0)
print(findMedianSortedArrays([1, 2], [3, 4]), 2.5)

"""

"""
