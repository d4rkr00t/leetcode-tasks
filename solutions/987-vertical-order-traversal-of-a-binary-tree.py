# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    groups = {}
    queue = [(root, 0, 0)]

    while queue:
        cur, level, depth = queue.pop(0)
        groups[level] = groups.get(level, [])
        groups[level].append((depth, cur.val))

        if cur.left:
            queue.append((cur.left, level - 1, depth + 1))

        if cur.right:
            queue.append((cur.right, level + 1, depth + 1))

    return [(item[1] for item in sorted(groups[key])) for key in sorted(groups.keys())]
