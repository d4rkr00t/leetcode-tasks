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

def findReplaceString(S: str, indexes: [int], sources: [str], targets: [str]) -> str:
    offset = 0

    for i,s,t in sorted(zip(indexes, sources, targets)):
        if S.startswith(s, i + offset):
            S = S[:i+offset] + t + S[i+len(s)+offset:]
            offset = offset + len(t) - len(s)

    return S

print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]), "eeebffff")
print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]), "eeecd")
