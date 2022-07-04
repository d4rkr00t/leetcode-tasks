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
    ans = 0

    def dfs(node):
        nonlocal ans

        if not node:
            return -1

        ldepth = 1 + dfs(node.left)
        rdepth = 1 + dfs(node.right)
        ans = max(ans, ldepth + rdepth)

        return max(ldepth, rdepth)

    dfs(root)

    return ans
