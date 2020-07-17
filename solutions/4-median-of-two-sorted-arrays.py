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

def findMedianSortedArrays(A: [int], B: [int]) -> float:
    m, n = len(A), len(B)
    if m > n:
        return findMedianSortedArrays(B, A)

    if n == 0:
        return None

    imin, imax, half_len = 0, m, (m+n+1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and B[j-1] > A[i]:
            # i is to small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is to big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])

            if (m+n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


print(findMedianSortedArrays([1, 3], [2]), 2.0)
print(findMedianSortedArrays([1, 2], [3, 4]), 2.5)

# nums1 = [1, 3]
# nums2 = [2]
#
