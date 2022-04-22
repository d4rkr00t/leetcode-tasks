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
        self.stack = []
        self.__populate_stack__(root)

    def __populate_stack__(self, node):
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        smlst = self.stack.pop()
        if smlst.right:
            self.__populate_stack__(smlst.right)

        return smlst.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
