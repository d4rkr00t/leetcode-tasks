# Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(
        root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

    seen = set()
    added = set()
    ans = []

    def dfs(node):
        if not node:
            return "X"

        left = dfs(node.left)
        right = dfs(node.right)
        cur = str(node.val)
        key = "|".join([left, right, cur])

        if key in seen and key not in added:
            ans.append(node)
            added.add(key)

        seen.add(key)

        return key

    dfs(root)

    return ans


# [0,0,0,0,null,null,0,null,null,|0]

#              0
#          0
#    0       0
# 0     0
#x x   x x
