# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# easy
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    def check(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return check(left.right, right.left) and check(left.left, right.right)

    return check(root, root)
