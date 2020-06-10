# Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def binaryTreePaths(self, root: TreeNode) -> List[str]:
    ans = []
    def dfs(s, root):
        nonlocal ans

        if not root:
            return

        s = s + "->" + str(root.val) if s else str(root.val)
        if not root.left and not root.right:
            ans.append(s)
        else:
            dfs(s, root.left)
            dfs(s, root.right)

    dfs("", root)

    return list(ans);

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
