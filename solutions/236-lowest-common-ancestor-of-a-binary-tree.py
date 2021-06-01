# Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                         q: TreeNode) -> TreeNode:
    def find(node, p, q):
        if not node:
            return False

        if node == p or node == q:
            return node

        left = find(node.left, p, q)
        right = find(node.right, p, q)

        if left and right:
            return node

        return left if left else right

    return find(root, p, q)
