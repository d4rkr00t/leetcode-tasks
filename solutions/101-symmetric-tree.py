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
    def check(node1, node2):
        if not node1 and not node2:
            return True

        if node1 == None or node2 == None:
            return False

        return node1.val == node2.val and check(node1.right, node2.left) and check(node2.right, node1.left)

    return check(root, root)
