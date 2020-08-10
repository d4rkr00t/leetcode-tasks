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
# TBD

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.__process__(root)

    def __process__(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.stack.pop()
        self.__process__(val.right)
        return val.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
