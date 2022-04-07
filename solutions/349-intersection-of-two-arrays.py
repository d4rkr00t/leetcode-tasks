# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    n1s = set(nums1)
    ans = set()

    for n in nums2:
        if n in n1s:
            ans.add(n)

    return list(ans)


print(intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2])
print(intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4])