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

    def calc(root):
        nonlocal ans

        if not root:
            return float("-inf")

        left = calc(root.left)
        right = calc(root.right)
        cur = max(root.val, root.val + left, root.val + right)

        ans = max(ans, root.val + left + right, left, right, cur)

        return cur

    calc(root)

    return ans
