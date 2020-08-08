# Find Permutation
# https://leetcode.com/problems/find-permutation/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findPermutation(s: str) -> List[int]:
    stack = []
    res = []

    for j in range(1, len(s)+1):
        if s[j-1] == "I":
            stack.append(j)
            while stack:
                res.append(stack.pop())
        else:
            stack.append(j)

    stack.append(len(s) + 1)

    while stack:
        res.append(stack.pop())

    return res


print(findPermutation("DI"), [2, 1, 3])
print(findPermutation("DDIIDI"), [3, 2, 1, 4, 6, 5, 7])
