# Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# easy
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(root):
        if not root:
            return 0

        return 1 + max(dfs(root.left), dfs(root.right))

    return max(dfs(root.left) + dfs(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
