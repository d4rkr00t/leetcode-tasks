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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    def is_valid(node, lo, hi):
        if not node:
            return True

        if node.val <= lo or node.val >= hi:
            return False

        return is_valid(node.left, lo, node.val) and is_valid(node.right, node.val, hi)

    return is_valid(root, float("-inf"), float("inf"))
