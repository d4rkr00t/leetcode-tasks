# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# easy
#
# Tags:
#
# Time:  O(N * log(N)) where n is max(nums1, nums2)
# Space: O(1)
#
# Solution:
# TBD

def intersection(nums1: [int], nums2: [int]) -> [int]:
    nums1.sort()
    nums2.sort()
    out = []

    i = j = 0

    while i < len(nums1) and j < len(nums2):
        ni = nums1[i]
        nj = nums2[j]

        if ni == nj:
            out.append(ni)
            i += 1
            j += 1
        elif ni > nj:
            j += 1
        else:
            i += 1

    return out



print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]), [2,2])
print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]), [9,4])
