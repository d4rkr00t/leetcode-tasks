# Erect the Fence
# https://leetcode.com/problems/erect-the-fence/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import functools


def outerTrees(trees: List[List[int]]) -> List[List[int]]:
    def orientation(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def distance(p, q):
        return pow((p[0] - q[0]), 2) + pow((p[1] - q[1]), 2)

    def bottomLeft():
        point = trees[0]

        for p in trees:
            if p[1] < point[1]:
                point = p

        return point

    start = bottomLeft()

    def compare(p, q):
        diff = orientation(start, p, q) - orientation(start, q, p)
        if diff == 0:
            return distance(start, p) - distance(start, q)

        return 1 if diff > 0 else -1

    if len(trees) <= 1:
        return trees

    trees.sort(key=functools.cmp_to_key(compare))

    i = len(trees) - 1
    while i >= 0 and orientation(start, trees[-1], trees[i]) == 0:
        i -= 1

        l = i + 1
        h = len(trees) - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1

        stack = []
        stack.append(trees[0])
        stack.append(trees[1])

        for j in range(2, len(trees)):
            top = stack.pop()
            while orientation(stack[-1], top, trees[j]) > 0:
                top = stack.pop()

            stack.append(top)
            stack.append(trees[j])

        return stack


print(outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]),
      [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]])
print(outerTrees([[1, 2], [2, 2], [4, 2]]), [[4, 2], [2, 2], [1, 2]])
