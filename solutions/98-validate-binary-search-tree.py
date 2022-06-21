# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# medium
#
# Tags: Amazon, Facebook, Microsoft, Google
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


def isValidBST(root: TreeNode) -> bool:
    def validate(node, min, max):
        if not node:
            return True

        if node.val <= min or node.val >= max:
            return False

        return validate(node.left, min, node.val) and validate(
            node.right, node.val, max)

    return validate(root, float("-inf"), float("inf"))
