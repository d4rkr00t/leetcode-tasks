# Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# medium
#
# Tags: Amazon, Microsoft, Facebook
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


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    res = []
    queue = deque([(root, 0)])
    tmp = []

    while queue:
        cur, lvl = queue.popleft()
        if lvl == len(res):
            tmp.append(cur.val)
        else:
            if len(res) % 2 == 1:
                tmp.reverse()
            res.append(tmp)
            tmp = [cur.val]

        if cur.left:
            queue.append((cur.left, lvl + 1))

        if cur.right:
            queue.append((cur.right, lvl + 1))

    if len(res) % 2 == 1:
        tmp.reverse()

    res.append(tmp)

    return res
