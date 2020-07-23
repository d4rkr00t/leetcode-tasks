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
    lca = None

    def check(node):
        nonlocal lca
        if lca or not node:
            return False

        left = check(node.left)
        right = check(node.right)
        is_self = node == q or node == p

        if left and right:
            if not lca:
                lca = node
            return True

        if is_self and (left or right):
            if not lca:
                lca = node
            return True

        return left or right or is_self

    check(root)

    return lca
