# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(2^n)
# Space: O(2^n)
#
# Solution:
# TBD

def generateParenthesis(n: int) -> [str]:
    ans = set()

    def backtrack(s, n, open, close):
        if abs(open - close) > n or close > open:
            return

        if n == 0:
            ans.add(s)
            return

        backtrack(s + "(", n-1, open + 1, close)
        backtrack(s + ")", n-1, open, close + 1)

    backtrack("", n*2, 0, 0)

    return list(ans)

print(generateParenthesis(3), [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])
