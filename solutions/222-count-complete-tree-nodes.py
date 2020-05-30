# Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# medium
#
# Tags: Google, Amazon
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

def countNodes(root: TreeNode) -> int:
    return 1 + countNodes(root.right) + countNodes(root.left) if root else 0


# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6
