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


def findReplaceString(S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
    pass


print(findReplaceString(S="abcd", indexes=[0, 2], sources=[
      "a", "cd"], targets=["eee", "ffff"]), "eeebffff")
print(findReplaceString(S="abcd", indexes=[0, 2], sources=[
      "ab", "ec"], targets=["eee", "ffff"]), "eeecd")
