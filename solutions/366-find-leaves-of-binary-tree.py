# Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from turtle import right
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    def dfs(node):
        if not node:
            return -1

        height = max(dfs(node.left), dfs(node.right)) + 1

        if height >= len(res):
            res.append([])

        res[height].append(node.val)
        return height

    dfs(root)
    return res
