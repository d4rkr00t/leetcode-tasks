# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# BFS

def rightSideView(self, root: TreeNode) -> List[int]:
    if not root: return []
    q = [(root, 0)]
    prev = None
    ans = []

    while q:
        node, level = q.pop(0)

        if prev and prev[1] != level:
            ans.append(prev[0].val)

        prev = (node, level)

        if node.left:
            q.append((node.left, level + 1))

        if node.right:
            q.append((node.right, level + 1))

        if not q:
            ans.append(node.val)

    return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

#
#     1
#   /   \
#  2     3
#   \
#    4
