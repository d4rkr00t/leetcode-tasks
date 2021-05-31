# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# medium
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n) – n is number of nodes
# Space: O(h) – h is height of the tree
#
# Solution:
# Recursion


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    def validate(node, minVal, maxVal):
        if not node:
            return True

        if minVal >= node.val or maxVal <= node.val:
            return False

        return validate(node.left, minVal, node.val) and validate(
            node.right, node.val, maxVal)

    return validate(root, float("-inf"), float("inf"))
