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

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    view = []
    stack = [root]

    while stack:
        view.append(stack[-1].val)
        next_layer = []

        for node in stack:
            if node.left:
                next_layer.append(node.left)

            if node.right:
                next_layer.append(node.right)

        stack = next_layer

    return view
