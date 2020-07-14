# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# medium
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    level = [root]
    ans = []

    while level:
        next_level = []

        ans.append(level[-1].val)

        for n in level:
            if n.left:
                next_level.append(n.left)

            if n.right:
                next_level.append(n.right)

        level = next_level

    return ans
