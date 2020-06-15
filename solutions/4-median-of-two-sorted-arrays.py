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

def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    m = len(nums1)
    n = len(nums2)

    if m > n:
        return findMedianSortedArrays(nums2, nums1)

    imin = 0
    imax = m
    half_len = (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1

        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1

        else:
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])

            if (n+m) % 2 == 1:
                return float(max_of_left)

            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0


print(findMedianSortedArrays([1, 3], [2]), 2.0)
print(findMedianSortedArrays([1, 2], [3,4]), 2.5)
print(findMedianSortedArrays([1, 2, 4], [3, 5, 6]), 3.5)

