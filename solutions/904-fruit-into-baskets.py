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

from typing import List
import collections


def totalFruit(tree: List[int]) -> int:
    count = collections.Counter()
    i = ans = 0

    for j in range(len(tree)):
        fruit = tree[j]
        count[fruit] += 1

        while len(count.keys()) > 2:
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1

        ans = max(ans, j-i+1)

    return ans


print(totalFruit([1, 2, 1]), 3)
print(totalFruit([0, 1, 2, 2]), 3)
print(totalFruit([1, 2, 3, 2, 2]), 4)
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)
