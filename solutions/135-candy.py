# Candy
# https://leetcode.com/problems/candy/
# hard
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def candy(ratings: List[int]) -> int:
    children = [1] * len(ratings)

    for i in range(1, len(children)):
        if ratings[i] > ratings[i - 1]:
            children[i] = 1 + children[i - 1]

    for i in range(len(children) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            children[i] = max(1 + children[i + 1], children[i])

    return sum(children)


print(candy([1, 0, 2]), 5)
print(candy([1, 2, 2]), 4)
print(candy([1, 3, 4, 5, 2]), 11)
# 1,3,4,5,2
# 1 2 3 4 1
