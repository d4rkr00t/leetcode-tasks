# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
from collections import Counter


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    cc = Counter(nums1)
    res = []

    for n in nums2:
        if cc[n] > 0:
            res.append(n)
        cc[n] -= 1

    return res


print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2, 2])
print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4])
