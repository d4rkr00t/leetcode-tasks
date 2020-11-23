# Next Permutation
# https://leetcode.com/problems/next-permutation/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1. find strongly decreasing sub seq i:j
    # 2. find next smallest number that is bigger than i-1 – k
    # 3. swap i-1 and k
    # 4. reverse i:j

    n = len(nums)
    start = end = n - 1

    while start > 0 and nums[start - 1] >= nums[start]:
        start -= 1

    if start == 0:
        nums.reverse()
        return nums

    k = end
    for i in range(end, start - 1, -1):
        if nums[i] > nums[start - 1]:
            k = i
            break

    nums[start - 1], nums[k] = nums[k], nums[start - 1]

    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

    return nums


print(nextPermutation([1, 2, 3]), [1, 3, 2])
print(nextPermutation([3, 2, 1]), [1, 2, 3])
print(nextPermutation([1, 1, 5]), [1, 5, 1])
