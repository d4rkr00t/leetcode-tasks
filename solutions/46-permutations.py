# Permutations
# https://leetcode.com/problems/permutations/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(n!)
# Space: O(n!)
#
# Solution:
# TBD

def permute(nums: [int]) -> [[int]]:
    ans = []
    def backtrack(cur, options):
        if not options:
            ans.append(cur)

        for i,o in enumerate(options):
            backtrack([] + cur + [o], options[:i] + options[i+1:])

    backtrack([],nums)

    return ans

print(permute([1,2,3]), [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
])
