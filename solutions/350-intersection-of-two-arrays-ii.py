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

import collections


def intersect(nums1: [int], nums2: [int]) -> [int]:
    count = collections.Counter(nums2)
    ans = []

    for n in nums1:
        if n in count and count[n] > 0:
            ans.append(n)
            count[n] -= 1

    return ans


print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2, 2])
print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4])
