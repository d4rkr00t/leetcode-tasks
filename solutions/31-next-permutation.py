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


def nextPermutation(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(nums, idx):
        end = len(nums) - 1
        while idx < end:
            nums[idx], nums[end] = nums[end], nums[idx]
            idx += 1
            end -= 1

    # 1. Find strongly decreasing subsequence
    idx = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            idx = i

    # 2. Take index before
    if idx == 0:
        reverse(nums, 0)
        return nums

    # 3. Find next largest item that is bigger than 2
    prev = idx - 1
    next = len(nums) - 1
    while nums[prev] >= nums[next]:
        next -= 1

    # 4. Swap [2] and [3]
    nums[prev], nums[next] = nums[next], nums[prev]

    # 5. reverse [1]
    reverse(nums, idx)

    return nums


print(nextPermutation([1, 2, 3]), [1, 3, 2])
print(nextPermutation([3, 2, 1]), [1, 2, 3])
print(nextPermutation([1, 1, 5]), [1, 5, 1])

# 1 2 5 4 3
# 1 3 2 4 5
