# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Stack


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.__add__(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.stack:
            return None

        item = self.stack.pop()
        if item.right:
            self.__add__(item.right)

        return item.val

    def __add__(self, node):
        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
