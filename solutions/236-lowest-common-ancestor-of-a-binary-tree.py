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


def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                         q: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return None

        selfMatch = node == p or node == q
        left = dfs(node.left)
        right = dfs(node.right)

        if selfMatch or (left and right):
            return node

        return left or right

    return dfs(root)
