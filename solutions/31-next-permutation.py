# Next Permutation
# https://leetcode.com/problems/next-permutation/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1. find decreasing subseq
    n = len(nums)-1
    while n > 0 and nums[n] <= nums[n-1]:
        n -= 1

    # 2. find next bigger item than 2
    if n == 0:
        nums.reverse()
        return nums

    # 3. Find next largest item that is bigger than 2
    prev = n - 1
    next = len(nums) - 1
    while nums[prev] >= nums[next]:
        next -= 1

    # 4. swap 2 and 3
    nums[prev], nums[next] = nums[next], nums[prev]

    hi = len(nums)-1
    while n < hi:
        nums[n], nums[hi] = nums[hi], nums[n]
        n += 1
        hi -= 1

    return nums


print(nextPermutation([1, 2, 3]), [1, 3, 2])
print(nextPermutation([3, 2, 1]), [1, 2, 3])
print(nextPermutation([1, 1, 5]), [1, 5, 1])

# 1, 2, 3, 4, 3, 2
# 1, 2, 4, 3, 3, 2
