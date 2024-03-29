# Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections
from typing import List


def totalFruit(tree: List[int]) -> int:
    a = cur = b = countB = res = 0

    for c in tree:
        cur = cur + 1 if c in (a, b) else countB + 1
        countB = countB if c == b else 1
        if b != c:
            a, b = b, c
        res = max(res, cur)

    return res


print(totalFruit([1, 2, 1]), 3)
print(totalFruit([0, 1, 2, 2]), 3)
print(totalFruit([1, 2, 3, 2, 2]), 4)
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)
