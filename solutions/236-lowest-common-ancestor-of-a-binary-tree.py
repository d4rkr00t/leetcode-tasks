# Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return False

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if (root == p or root == q) and not left and not right:
        return True

    if (root == p or root == q) and (left or right):
        return root

    if left and right:
        return root

    return left or right
