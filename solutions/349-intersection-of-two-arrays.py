# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n + m)
# Space: O(min(n, m))

def intersection(nums1: [int], nums2: [int]) -> [int]:
    if len(nums1) > len(nums2):
        return intersection(nums2, nums1)

    nums1 = set(nums1)
    ans = set()

    for n in nums2:
        if n in nums1:
            ans.add(n)

    return list(ans)

print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]), [2])
print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]), [9,4])

