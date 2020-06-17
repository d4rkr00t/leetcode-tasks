# Subsets
# https://leetcode.com/problems/subsets/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(2^N)
# Space: O(2^n)
#
# Solution:
# TBD

def subsets(nums: [int]) -> [[int]]:
    out = [[]]

    for n in nums:
        out += [s + [n] for s in out]

    return out


print(subsets([1,2,3]), [
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
])
