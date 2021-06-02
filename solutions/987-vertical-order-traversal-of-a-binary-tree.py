# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  O(N)
# Space: O(N)
#
# Solution:
# TBD

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    levels = {}

    if not root:
        return []

    queue = [(root, 0)]
    while queue:
        cur, lvl = queue.pop(0)
        levels[lvl] = levels.get(lvl, [])
        levels[lvl].append(cur.val)

        if cur.left:
            queue.append((cur.left, lvl - 1))

        if cur.right:
            queue.append((cur.right, lvl + 1))

    ans = []
    for i in sorted(levels.keys()):
        ans.append(levels[i])

    return ans
