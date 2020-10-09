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

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    queue = [root]
    ans = []
    dir = 1

    while queue:
        next_level = []
        tmp = []

        while queue:
            cur = queue.pop(0)
            tmp.append(cur.val)
            if cur.left:
                next_level.append(cur.left)

            if cur.right:
                next_level.append(cur.right)

        if dir == 1:
            dir = -1
        else:
            tmp.reverse()
            dir = 1

        ans.append(tmp)
        queue = next_level

    return ans

# [1,2,3,4,null,null,5]

#     1
#   2   3
# 4      5
