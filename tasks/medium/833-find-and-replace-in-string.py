# Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findReplaceString(s: str, indices: List[int], sources: List[str],
                      targets: List[str]) -> str:
    pass


print(
    findReplaceString(s="abcd",
                      indices=[0, 2],
                      sources=["a", "cd"],
                      targets=["eee", "ffff"]), "eeebffff")
print(
    findReplaceString(s="abcd",
                      indices=[0, 2],
                      sources=["ab", "ec"],
                      targets=["eee", "ffff"]), "eeecd")
