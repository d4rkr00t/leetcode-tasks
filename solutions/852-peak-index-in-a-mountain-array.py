# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# easy
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def peakIndexInMountainArray(A: List[int]) -> int:
    lo = 0
    hi = len(A) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if A[mid] < A[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return lo


print(peakIndexInMountainArray([0, 1]), 1)
print(peakIndexInMountainArray([0, 1, 0]), 1)
print(peakIndexInMountainArray([0, 2, 1, 0]), 1)
print(peakIndexInMountainArray([0, 2, 1, 1, 0]), 1)
print(peakIndexInMountainArray([0, 1, 1, 1, 2, 1, 1, 0]), 4)

# 0, 1, 1, 1, 2, 1, 1, 0
#          |  |

# 0 1 0
#   | |

# 0, 2, 1, 1, 0
# |     |     |
