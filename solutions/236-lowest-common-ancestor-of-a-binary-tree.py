# Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  O(n) – number of nodes in a tree
# Space: O(h) – height of a tree
#
# Solution:
# TBD

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root: return False

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    elif root != p and root != q and (left or right):
        return left or right

    return root if root == p or root == q else left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
