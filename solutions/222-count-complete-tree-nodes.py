# Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# medium
#
# Tags: Google, Amazon
#
# Time:  O(log^2(n))
# Space: O(1)
#
# Solution:
# TBD


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: TreeNode) -> int:
    def depth(root):
        d = 0
        while root:
            d += 1
            root = root.left

        return d

    def exists(idx, d, node):
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1

        return node is not None

    if not root:
        return 0

    d = depth(root)
    if d == 0:
        return 1

    left, right = 1, 2**d - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if exists(pivot, d, root):
            left = pivot + 1
        else:
            right = pivot - 1

    return (2**d - 1) + left


#         1
#      2    3
#    4   5
#
#
