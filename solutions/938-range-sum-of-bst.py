# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(node):
        if not node:
            return 0

        val = node.val
        if val >= low and val <= high:
            return val + dfs(node.left) + dfs(node.right)
        elif node.val <= low:
            return dfs(node.right)
        elif node.val >= high:
            return dfs(node.left)

        return 0

    return dfs(root)
