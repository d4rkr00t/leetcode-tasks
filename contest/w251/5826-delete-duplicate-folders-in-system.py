# Delete Duplicate Folders in System
# https://leetcode.com/contest/weekly-contest-251/problems/delete-duplicate-folders-in-system/
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


def deleteDuplicateFolder(paths: List[List[str]]) -> List[List[str]]:
    pass


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
