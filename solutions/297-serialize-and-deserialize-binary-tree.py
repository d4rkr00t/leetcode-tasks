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
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "X"

        return str(root.val) + "|" + self.serialize(
            root.left) + "|" + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split("|")
        (root, _) = self.__deserializeNode__(nodes, 0)
        return root

    def __deserializeNode__(self, nodes, idx):
        if idx >= len(nodes):
            return (None, idx)

        if nodes[idx] == "X":
            return (None, idx)

        node = TreeNode(int(nodes[idx]))
        (node.left, idx) = self.__deserializeNode__(nodes, idx + 1)
        (node.right, idx) = self.__deserializeNode__(nodes, idx + 1)

        return (node, idx)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
