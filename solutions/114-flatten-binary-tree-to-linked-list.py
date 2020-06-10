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
# DFS

def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def dfs(root):
        if not root:
            return (None, None)

        if not root.left and not root.right:
            return (root, root)

        left, leftLeaf = dfs(root.left)
        right, rightLeaf = dfs(root.right)

        root.left = None
        if left and leftLeaf:
            root.right = left
            leftLeaf.right = right

        return (root, rightLeaf or leftLeaf)

    dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
