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
            return 0

        depth = max(dfs(node.left), dfs(node.right))

        if depth >= len(res):
            res.append([])

        res[depth].append(node.val)

        return depth + 1

    dfs(root)

    return res
