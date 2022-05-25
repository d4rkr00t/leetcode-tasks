# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    prev_node = None
    prev_lvl = 0
    queue = deque([(root, 0)])
    ans = []

    while queue:
        cur, lvl = queue.popleft()

        if lvl != prev_lvl and prev_node:
            ans.append(prev_node.val)

        if cur.left: queue.append((cur.left, lvl + 1))
        if cur.right: queue.append((cur.right, lvl + 1))

        if not queue:
            ans.append(cur.val)

        prev_node = cur
        prev_lvl = lvl

    return ans
