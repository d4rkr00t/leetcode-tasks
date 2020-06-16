# Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def moveZeroes(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = -1

    for j in range(len(nums)):
        if nums[j] == 0:
            i = j if i < 0 or nums[i] != 0 else i
            continue

        if i >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


print(moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
print(moveZeroes([1,0,3,12,0]), [1,3,12,0,0])
print(moveZeroes([1,3,12]), [1,3,12])
print(moveZeroes([1,0]), [0,1])

# 1 3 0 0 12
#     i
#         j
