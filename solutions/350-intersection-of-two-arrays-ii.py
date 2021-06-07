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
import collections


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counter = collections.Counter(nums1)
    ans = []

    for n in nums2:
        if counter[n] > 0:
            ans.append(n)
            counter[n] -= 1

    return ans


print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2, 2])
print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4])
