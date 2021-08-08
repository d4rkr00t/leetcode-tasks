# Delete Duplicate Folders in System
# https://leetcode.com/problems/delete-duplicate-folders-in-system/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.dl = False


def deleteDuplicateFolder(paths):
    def dfs1(node):
        key = "(" + "".join(c + dfs1(node.child[c]) for c in node.child) + ")"
        if key != "()": pattern[key].append(node)
        return key

    def dfs2(node, path):
        for c in node.child:
            if not node.child[c].dl:
                dfs2(node.child[c], path + [c])
        if path: ans.append(path[:])

    pattern, root, ans = defaultdict(list), Node(), []

    for path in sorted(paths):
        node = root
        for c in path:
            node = node.child[c]

    dfs1(root)

    for nodes in pattern.values():
        if len(nodes) > 1:
            for i in nodes:
                i.dl = True

    dfs2(root, [])
    return ans


print(
    deleteDuplicateFolder([["a"], ["c"], ["d"], ["a", "b"], ["c", "b"],
                           ["d", "a"]]), [["d"], ["d", "a"]])
print(
    deleteDuplicateFolder([["a"], ["c"], ["a", "b"], ["c", "b"],
                           ["a", "b", "x"], ["a", "b", "x", "y"], ["w"],
                           ["w", "y"]]),
    [["c"], ["c", "b"], ["a"], ["a", "b"]])
print(deleteDuplicateFolder([["a", "b"], ["c", "d"], ["c"], ["a"]]),
      [["c"], ["c", "d"], ["a"], ["a", "b"]])
print(
    deleteDuplicateFolder([["a"], ["a", "x"], ["a", "x", "y"], ["a",
                                                                "z"], ["b"],
                           ["b", "x"], ["b", "x", "y"], ["b", "z"]]), [])
