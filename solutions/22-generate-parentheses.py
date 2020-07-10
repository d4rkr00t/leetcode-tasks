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


def generateParenthesis(n: int) -> [str]:
    ans = []

    def backtrack(s, n, o, c):
        nonlocal ans

        if c > o or o - c > n:
            return

        if n == 0:
            return ans.append(s)

        backtrack(s + ")", n-1, o, c+1)
        backtrack(s + "(", n-1, o+1, c)

    backtrack("", n*2, 0, 0)

    return ans


print(generateParenthesis(3), [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])
