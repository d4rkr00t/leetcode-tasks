# Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Recursion

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(self, root: TreeNode) -> List[str]:
    ans = []

    def dfs(node, path):
        if not node:
            return

        path = path + [str(node.val)]

        if not node.left and not node.right:
            ans.append("->".join(path))
            return

        dfs(node.left, [] + path)
        dfs(node.right, [] + path)

    dfs(root, [])

    return ans
