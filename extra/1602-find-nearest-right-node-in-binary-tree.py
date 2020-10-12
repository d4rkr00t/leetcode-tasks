# Find Nearest Right Node in Binary Tree
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# medium
#
# Tags: Google
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


def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
    level = [root]

    if root == u:
        return None

    while level:
        in_this_level = False
        next_level = []

        while level:
            cur = level.pop(0)

            if cur.left:
                next_level.append(cur.left)

            if cur.right:
                next_level.append(cur.right)

            if cur.left == u or cur.right == u:
                in_this_level = True

        if in_this_level:
            idx = next_level.index(u)

            if idx < len(next_level) - 1:
                return next_level[idx + 1]
            else:
                return None

        level = next_level

    return None
