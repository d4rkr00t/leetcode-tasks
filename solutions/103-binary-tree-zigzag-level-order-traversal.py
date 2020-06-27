# Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(level)
#
# Solution:
# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def zigzagLevelOrder(root: TreeNode) -> [[int]]:
    if not root: return []
    level = [root]
    result = [[root.val]]
    d = 0

    while level:
        next_level = []

        for n in level:
            if n.left: next_level.append(n.left)
            if n.right: next_level.append(n.right)

        if next_level:
            result.append([n.val for n in (next_level if d == 1 else next_level[::-1])])
        level = next_level
        d = 1 ^ d

    return result

