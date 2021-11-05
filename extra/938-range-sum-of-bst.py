# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# easy
#
# Tags:
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


def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(node):
        if not node:
            return 0

        if low <= node.val <= high:
            return node.val + dfs(node.right) + dfs(node.left)
        elif node.val <= low:
            return dfs(node.right)
        elif node.val >= high:
            return dfs(node.left)

        return 0

    return dfs(root)
