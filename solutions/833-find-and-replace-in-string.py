# Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/
# medium
#
# Tags: Google
#
# Time:  O(op*n)
# Space: O(1)

from typing import List


def findReplaceString(S: str, indexes: List[int], sources: List[str],
                      targets: List[str]) -> str:
    for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
        if S.startswith(s, i):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S

    return S


print(
    findReplaceString(S="abcd",
                      indexes=[0, 2],
                      sources=["a", "cd"],
                      targets=["eee", "ffff"]), "eeebffff")
print(
    findReplaceString(S="abcd",
                      indexes=[0, 2],
                      sources=["ab", "ec"],
                      targets=["eee", "ffff"]), "eeecd")
