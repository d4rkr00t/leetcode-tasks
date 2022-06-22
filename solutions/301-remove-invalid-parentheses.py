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
    removed = float("inf")

    def backtrack(ss, pos, op, cl, rem):
        nonlocal ans, removed
        if cl > op:
            return

        if pos == len(s):
            if op != cl: return
            if rem == removed:
                ans.add("".join(ss))
                return
            if rem < removed:
                ans = set(["".join(ss)])
                removed = rem
            return

        cur = s[pos]

        if cur in (")", "("):
            backtrack(ss, pos + 1, op, cl, rem + 1)

            ss.append(cur)
            nOp = op + 1 if cur == "(" else op
            nCl = cl + 1 if cur == ")" else cl
            backtrack(ss, pos + 1, nOp, nCl, rem)
            ss.pop()
        else:
            ss.append(cur)
            backtrack(ss, pos + 1, op, cl, rem)
            ss.pop()

    backtrack([], 0, 0, 0, 0)
    return list(ans)


print(removeInvalidParentheses("()())()"), ["()()()", "(())()"])
print(removeInvalidParentheses("(a)())()"), ["(a)()()", "(a())()"])
print(removeInvalidParentheses(")("), [""])
