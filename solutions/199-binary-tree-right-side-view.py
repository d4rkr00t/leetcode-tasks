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

    queue = deque([(root, 0)])
    prev_lvl = 0
    prev_node = None
    ans = []

    while queue:
        cur, lvl = queue.popleft()
        if lvl != prev_lvl:
            prev_lvl = lvl
            ans.append(prev_node.val)

        prev_node = cur
        if cur.left: queue.append((cur.left, lvl + 1))
        if cur.right: queue.append((cur.right, lvl + 1))

    ans.append(prev_node.val)

    return ans
