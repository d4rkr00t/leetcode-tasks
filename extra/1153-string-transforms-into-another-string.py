# String Transforms Into Another String
# https://leetcode.com/problems/string-transforms-into-another-string/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import Deque


def canConvert(str1: str, str2: str) -> bool:
    g = {c: None for c in "abcdefghijklmnopqrstuvwxyz"}

    for i, c in enumerate(str1):
        if g[c] and g[c] != str2[i]: return False
        g[c] = str2[i]

    visit = set()
    breaker = 0
    cycles = 0

    def dfs(cur, st):
        nonlocal breaker, cycles
        st.append(cur)
        visit.add(cur)

        if g[cur] not in g:
            breaker += 1  # If we can't go over, this is a non-cyclic component.
            return

        if g[cur] not in visit:
            dfs(g[cur], st)
        elif g[cur] in st:
            # If next alphabet already exists in the stack, we found cycle.
            if len(st) > 1:
                cycles += 1  # We don't consider self-conversion (len(st) == 1) as cycle.
            if st[0] != g[cur]:
                breaker += 1  # If there are some nodes which are not belonging to the cycle, they are non-cyclic components.

    for c in g:
        if c not in visit:
            dfs(c, Deque())

    return cycles == 0 or breaker > 0


print(canConvert(str1="ab", str2="ba"), True)
print(canConvert(str1="aabcc", str2="ccdee"), True)
print(canConvert(str1="leetcode", str2="codeleet"), False)
print(
    canConvert(str1="abcdefghijklmnopqrstuvwxyz",
               str2="bcdefghijklmnopqrstuvwxyza"), False)

# bcdefghijklmnopqrstuvwxyza
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz

# a -> b -> c
