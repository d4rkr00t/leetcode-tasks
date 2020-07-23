# Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:
    def max_gain(node):
        nonlocal max_sum

        if not node:
            return 0

        left = max(max_gain(node.left), 0)
        right = max(max_gain(node.right), 0)

        newpath = node.val + left + right

        max_sum = max(max_sum, newpath)

        return node.val + max(left, right)

    max_sum = 0

    max_gain(root)

    return max_sum
