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
    next = None

    def flat(root):
        nonlocal next
        if not root:
            return None

        if next:
            next.right = root

        next = root
        left = root.left
        right = root.right

        root.left = None

        flat(left)
        flat(right)

    flat(root)
