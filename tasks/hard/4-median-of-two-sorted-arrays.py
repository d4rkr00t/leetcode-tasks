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
    n1_len = len(nums1)
    n2_len = len(nums2)

    if n1_len > n2_len:
        return findMedianSortedArrays(nums2, nums1)

    half_len = (n1_len + n2_len + 1) // 2
    imin = 0
    imax = n1_len

    while imax >= imin:
        i = (imax + imin) // 2
        j = half_len - i

        if i < n1_len and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0: max_of_left = nums2[j - 1]
            elif j == 0: max_of_left = nums1[i - 1]
            else: max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (n1_len + n2_len) % 2 == 1:
                return float(max_of_left)

            if i == n1_len: min_of_right = nums2[j]
            elif j == n2_len: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (min_of_right + max_of_left) / 2.0


print(findMedianSortedArrays([1, 3], [2]), 2.0)
print(findMedianSortedArrays([1, 2], [3, 4]), 2.5)
print(findMedianSortedArrays([1, 2, 4, 6], [3, 5, 7, 8]), 4.5)

# A = [1,2,4,6]
# B = [3,5,7,8]
# half_len = (4 + 4 + 1) // 2 = 4
# imin = 0
# imax = len(A) = 4
# i = (imax + imin) // 2 = 2
# j = half_len - i = 4 - 2 = 2
#
# A = [1,2] [4,6]
# B = [3,5] [7,8]
#
# L_MAX = 5
# R_MIN = 4
#
# i = i+1 = 3
# j = half_len - i = 4 - 3 = 1
#
# A = [1,2,4] [6]
# B = [3] [5,7,8]
#
# L_MAX = 4
# R_MIN = 5
# ANS = (4 + 5) / 2 = 4.5
