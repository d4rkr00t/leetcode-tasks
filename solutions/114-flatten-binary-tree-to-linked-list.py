# Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(n)
# Space: O(h)
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
    last = None

    def flat(node):
        nonlocal last
        left = node.left
        right = node.right
        node.left = None
        node.right = None

        if last:
            last.right = node

        last = node
        flat(left)
        flat(right)

    flat(root)

    return root


#    1 -> 2 ->
#   |
#   |      1
# > |   2     5
#   | 3   4     6
#   |
