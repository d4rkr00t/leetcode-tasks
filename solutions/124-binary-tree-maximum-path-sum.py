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
    ans = float("-inf")

    def dfs(node):
        nonlocal ans

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        ans = max(ans, node.val + left + right)

        return max(node.val + left, node.val + right)

    dfs(root)

    return ans
