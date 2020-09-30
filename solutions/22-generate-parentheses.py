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

    def backtrack(cur, o, c):
        if len(cur) == n * 2:
            if o == c:
                ans.append("".join(cur))
            return

        if o + 1 <= n:
            cur.append("(")
            backtrack(cur, o+1, c)
            cur.pop()

        if c + 1 <= n and c < o:
            cur.append(")")
            backtrack(cur, o, c+1)
            cur.pop()

    backtrack([], 0, 0)

    return ans


print(generateParenthesis(3), [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])

print(generateParenthesis(2), [
    "(())",
    "()()",
])
