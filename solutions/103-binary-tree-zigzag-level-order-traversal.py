# Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n+h)
# Space: O(n)
#
# Solution:
# TBD

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    ans = []
    queue = [(0, root)]

    while queue:
        lvl, cur = queue.pop(0)
        if len(ans) == lvl:
            ans.append([])

        ans[lvl].append(cur.val)

        if cur.left:
            queue.append((lvl+1, cur.left))

        if cur.right:
            queue.append((lvl+1, cur.right))

    for i in range(len(ans)):
        if i % 2 == 1:
            ans[i].reverse()

    return ans
