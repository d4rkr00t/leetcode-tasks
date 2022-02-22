# Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(self, root: TreeNode) -> List[str]:
    def dfs(node):
        if not node:
            return []

        cur = str(node.val)

        if not node.left and not node.right:
            return [cur]

        res = []
        for p in dfs(node.left):
            res.append(cur + "->" + p)

        for p in dfs(node.right):
            res.append(cur + "->" + p)

        return res

    return dfs(root)
