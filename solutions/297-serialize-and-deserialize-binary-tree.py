# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __preorder_serialize__(self, node, res):
        if not node:
            res.append("X")
            return

        res.append(str(node.val))
        self.__preorder_serialize__(node.left, res)
        self.__preorder_serialize__(node.right, res)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.__preorder_serialize__(root, res)
        return "|".join(res)

    def __preorder_deserialize__(self, data):
        if not data:
            return

        val = data.pop(0)
        if val == "X":
            return None

        node = TreeNode(int(val))

        node.left = self.__preorder_deserialize__(data)
        node.right = self.__preorder_deserialize__(data)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        d = data.split("|")
        return self.__preorder_deserialize__(d)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# 1 2 3 null null 4 5 null null null null
