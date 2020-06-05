# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# easy
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(log(n))
# Space: O(1)
#
# Solution:
# Binary Search

def peakIndexInMountainArray(A: [int]) -> int:
    lo, hi = 0, len(A) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if A[mid] < A[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return lo

print(peakIndexInMountainArray([0,1,0]), 1)
print(peakIndexInMountainArray([0,2,1,0]), 1)

# 1 2 3 4 5 6 4 3 2 1
