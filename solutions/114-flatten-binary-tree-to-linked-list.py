# Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    last = root

    def dfs(node):
        nonlocal last
        if not node:
            return

        left = node.left
        right = node.right
        last.right = node
        last = node
        node.left = None
        node.right = None

        dfs(left)
        dfs(right)

    dfs(root)

    return root
