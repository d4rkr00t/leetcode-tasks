# Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
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


def maxPathSum(root: TreeNode) -> int:
    if not root:
        return 0

    ans = root.val

    def dfs(node):
        nonlocal ans
        if not node:
            return 0

        val = node.val

        left = dfs(node.left)
        right = dfs(node.right)

        ans = max(ans, val, val + left + right, val + left, val + right)

        return max(val, val + left, val + right)

    dfs(root)

    return ans
