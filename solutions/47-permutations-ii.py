# Permutations II
# https://leetcode.com/problems/permutations-ii/
# medium
#
# Tags: Amazon
#
# Time:  O(n!)
# Space: O(n!)
#
# Solution:
# TBD

def permuteUnique(nums: [int]) -> [[int]]:
    ans = set()

    def backtrack(nums, res):
        if not nums:
            ans.add(tuple(res))

        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], [] + res + [nums[i]])

    backtrack(nums, [])

    return [list(p) for p in list(ans)]

print(permuteUnique([1,1,2]), [
    [1,1,2],
    [1,2,1],
    [2,1,1]
])
