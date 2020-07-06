# Permutations
# https://leetcode.com/problems/permutations/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def permute(nums: [int]) -> [[int]]:
    ans = []

    def backtrack(first):
        nonlocal ans
        if first == len(nums):
            ans.append(nums[:])

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack(0)

    return ans


print(permute([1, 2, 3]), [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
])
