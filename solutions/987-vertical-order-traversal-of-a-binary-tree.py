# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  O(n*log(n))
# Space: O(n)
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
    levels = {}

    def dfs(node, row, col):
        if not node:
            return

        levels[col] = levels.get(col, [])
        levels[col].append((col, row, node.val))

        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    ans = [sorted(levels[key]) for key in sorted(levels.keys())]
    return [[v for c, r, v in level] for level in ans]
