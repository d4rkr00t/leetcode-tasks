# Subsets
# https://leetcode.com/problems/subsets/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n*2^n)
# Space: O(n*2^n)
#
# Solution:
# Bruteforce

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    out = [[]]

    for n in nums:
        out += [x + [n] for x in out]

    return out


print(subsets([1, 2, 3]),
      [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []])

# []
# [] [1]
# [] [1] [1, 2] [2]
# [] [1] [1, 2] [2] [3] [1,3] [1, 2, 3] [2 3]
