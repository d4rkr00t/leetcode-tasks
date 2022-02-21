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

from re import L
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def findDecreasing():
        idx = 0
        for i in range(len(nums)):
            prev = float("inf") if i == 0 else nums[i - 1]
            if prev < nums[i]:
                idx = i

        return idx - 1

    def findSmallestNumBiggerThan(k):
        diff = float("inf")
        idx = k
        for i in range(k, len(nums)):
            if nums[i] > nums[k] and abs(nums[i] - nums[k]) <= diff:
                idx = i
                diff = abs(nums[i] - nums[k])

        return idx

    k = findDecreasing()
    j = findSmallestNumBiggerThan(k)

    if k < 0:
        nums.reverse()
        return nums

    nums[k], nums[j] = nums[j], nums[k]

    start = k + 1
    end = len(nums) - 1
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

    return nums


print(nextPermutation([1, 3, 2]), [2, 1, 3])
# print(nextPermutation([1, 2, 3]), [1, 3, 2])
# print(nextPermutation([3, 2, 1]), [1, 2, 3])
# print(nextPermutation([1, 1, 5]), [1, 5, 1])
# print(nextPermutation([1, 4, 8, 10, 7, 6, 3]), [1, 4, 10, 3, 6, 7, 8])

# 1. find dec subseq
# 1, 4, 8, 10, 7, 6, 3
#       k   j
# 2. swap k and j
# 1, 4, 10, 8, 7, 6, 3
#        k
# 3. sort from k+1
# 1, 4, 10, 3, 6, 7, 8
