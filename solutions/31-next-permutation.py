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

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]

            start += 1
            end -= 1

        return arr

    N = len(nums) - 1

    # 1. find strongly decreasing subseqence
    start = N
    while start > 0 and nums[start-1] >= nums[start]:
        start -= 1

    if start == 0:
        return reverse(nums, 0, N)

    # 2. take a idx before the subsequence
    # 3. find next item wich is bigger than [2]
    next = N
    while next > 0 and nums[next] <= nums[start-1]:
        next -= 1

    # 4. swap [3] and [2]
    nums[start-1], nums[next] = nums[next], nums[start-1]

    # 5. reverse starting with [1]
    return reverse(nums, start, N)


print(nextPermutation([1,2,3]), [1,3,2])
print(nextPermutation([3,2,1]), [1,2,3])
print(nextPermutation([1,1,5]), [1,5,1])
print(nextPermutation([1,5,4,3]), [3,1,4,5])

[1,5,4,3]
[3,5,4,1]
