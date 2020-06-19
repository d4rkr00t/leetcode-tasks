# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# medium
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(h) where h is a hight of a tree
#
# Solution:
# TBD

def isValidBST(root: TreeNode) -> bool:
    def validate_node(node, low, high):
        if not node:
            return True

        if low >= node.val or node.val >= high:
            return False

        return validate_node(node.left, low, node.val) and validate_node(node.right, node.val, high)

    return validate_node(root, float("-inf"), float("inf"))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
