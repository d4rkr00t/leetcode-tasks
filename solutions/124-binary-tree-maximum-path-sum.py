# Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  O(N)
# Space: O(H)
#
# Solution:
# DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:
    ans = float("-inf")

    def max_sum(node):
        nonlocal ans

        if not node:
            return 0

        left = max_sum(node.left)
        right = max_sum(node.right)

        ans = max(ans, node.val + left + right)

        return max(node.val, node.val + left, node.val + right)

    max_sum(root)

    return ans
