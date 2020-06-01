# Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/
# medium
#
# Tags: Google
#
# Time:  O(S+N)
# Space: O(1)
#
# Solution:
# TBD

def findReplaceString(S: str, indexes: [int], sources: [str], targets: [str]) -> str:
    for i,s,t in sorted(zip(indexes, sources, targets), reverse=True):
        S = S[:i] + t + S[i + len(s):] if S[i:i+len(s)] == s else S
    return S

print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]), "eeebffff")
print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]), "eeecd")
