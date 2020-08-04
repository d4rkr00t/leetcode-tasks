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
    table = {}

    def dfs(node, level):
        nonlocal table

        if not node:
            return

        table[level] = table.get(level, [])
        table[level].append(node.val)

        dfs(node.left, level - 1)
        dfs(node.right, level + 1)

    dfs(root, 0)

    return [table[key] for key in sorted(table.keys())]
