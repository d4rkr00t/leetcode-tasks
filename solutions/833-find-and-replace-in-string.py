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


def findReplaceString(S: str, indexes: List[int], sources: List[str],
                      targets: List[str]) -> str:
    offset = 0
    for (idx, src, tgt) in sorted(zip(indexes, sources, targets)):
        pos = idx + offset
        if S[pos:].startswith(src):
            S = S[:pos] + tgt + S[pos + len(src):]
            offset += len(tgt) - len(src)

    return S


# print(
#     findReplaceString(S="abcd",
#                       indexes=[0, 2],
#                       sources=["a", "cd"],
#                       targets=["eee", "ffff"]), "eeebffff")
# print(
#     findReplaceString(S="abcd",
#                       indexes=[0, 2],
#                       sources=["ab", "ec"],
#                       targets=["eee", "ffff"]), "eeecd")

print(
    findReplaceString(S="vmokgggqzp",
                      indexes=[3, 5, 1],
                      sources=["kg", "ggq", "mo"],
                      targets=["s", "so", "bfr"]), "vbfrssozp")
