# Minimum Window Subsequence
# https://leetcode.com/problems/minimum-window-subsequence/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD
import collections


def minWindow(s1: str, s2: str) -> str:
    chpositions = collections.defaultdict(collections.deque)
    start = count = -1

    for i, ch in enumerate(s2):
        chpositions[ch].appendleft(i)  # we'll be iterating from last to first

    startpositions = [-1] * len(s2)
    for i, ch in enumerate(s1):
        if ch not in chpositions: continue
        for pos in chpositions[ch]:
            if pos == 0: startpositions[0] = i
            else: startpositions[pos] = startpositions[pos - 1]
            if pos == len(s2) - 1 and (start == -1
                                       or count > i - startpositions[-1] + 1):
                start = startpositions[-1]
                count = i - startpositions[-1] + 1

    if start < 0: return ''
    return s1[start:start + count]


# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5, 16, 16, 16, 16, 16],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16, 16, 16, 16, 16]

# print(minWindow(s1="abcdebddde", s2="bde"), "bcde")
print(minWindow(s1="jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2="u"), "")
print(minWindow(s1="cnhczmccqouqadqtmjjzl", s2="mm"), "mccqouqadqtm")
