# Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# medium
#
# Time:  O(n^2)
# Space: O(n)

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n: int) -> List[TreeNode]:
    def trees(first, last):
        res = []

        for root in range(first, last + 1):
            for left in trees(first, root - 1):
                for right in trees(root + 1, last):
                    res.append(TreeNode(root, left, right))

        return res or [None]

    return trees(1, n)


print(generateTrees(3))
print(generateTrees(2))
print(generateTrees(1))

# n = 1
# 1
#
# n = 2
# 1
#  \
#   2
#
#   2
#  /
# 1
#
# n = 3
#  2   2      2
# /     \   /   \
