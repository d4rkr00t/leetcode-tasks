# Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/
# hard
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def removeInvalidParentheses(s: str) -> List[str]:
    ans = set()
    min_removed = float("inf")

    def is_possible(pos, o, c):
        return o >= c and len(s) > pos + (o-c)

    def recur(cur, pos, o, c, removed):
        nonlocal ans, min_removed
        if pos == len(s):
            if removed <= min_removed and is_possible(pos-1, o, c):
                ans.add(cur)
                min_removed = removed
            return

        char = s[pos]

        if char != "(" and char != ")":
            return recur(cur + char, pos + 1, o, c, removed)

        uo = o + 1 if char == "(" else o
        uc = c + 1 if char == ")" else c

        if is_possible(pos, uo, uc):
            recur(cur + char, pos + 1, uo, uc, removed)

        if (is_possible(pos, o, c)):
            recur(cur, pos + 1, o, c, removed+1)

    recur("", 0, 0, 0, 0)

    return list(ans)


print(removeInvalidParentheses("()())()"), ["()()()", "(())()"])
print(removeInvalidParentheses("(a)())()"), ["(a)()()", "(a())()"])
print(removeInvalidParentheses(")("), [])
