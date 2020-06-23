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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def zigzagLevelOrder(root: TreeNode) -> [[int]]:
    if not root:
        return []
    level = [root]
    ans = [[root.val]]
    l = 0
    dir = 0

    while level:
        next_level = []

        for n in level:
            if n.left: next_level.append(n.left)
            if n.right: next_level.append(n.right)

        if next_level:
            ans.append([n.val for n in (next_level if dir else next_level[::-1])])

        level = next_level
        l += 1
        dir = l % 2

    return ans

#         0
#     2       4
#   1       3   -1
# 5   1        6   8
