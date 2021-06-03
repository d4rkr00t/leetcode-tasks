# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def generateParenthesis(n: int) -> List[str]:
    ans = []

    def backtrack(n, cur, o, c):
        if c > o:
            return

        if n == 0:
            if o == c:
                ans.append("".join(cur))
            return

        cur.append("(")
        backtrack(n - 1, cur, o + 1, c)
        cur.pop()

        cur.append(")")
        backtrack(n - 1, cur, o, c + 1)
        cur.pop()

    backtrack(n * 2, [], 0, 0)

    return ans


print(generateParenthesis(3),
      ["((()))", "(()())", "(())()", "()(())", "()()()"])

print(generateParenthesis(8))
