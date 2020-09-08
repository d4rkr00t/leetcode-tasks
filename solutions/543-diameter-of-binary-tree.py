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


def diameterOfBinaryTree(root: TreeNode, d=0) -> int:
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        cur = left + right
        ans = max(cur, ans)

        return max(left+1, right+1)

    dfs(root)

    return ans
