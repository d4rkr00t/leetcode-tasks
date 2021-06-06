# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  O(N)
# Space: O(D)

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root: TreeNode) -> List[int]:
    ans = []

    queue = [(root, 0)]
    prev = None
    prev_lvl = 0

    while queue:
        cur, lvl = queue.pop(0)

        if lvl != prev_lvl:
            ans.append(prev.val)

        prev = cur
        prev_lvl = lvl

        if cur.left:
            queue.append((cur.left, lvl + 1))

        if cur.right:
            queue.append((cur.right, lvl + 1))

    ans.append(prev.val)

    return ans
