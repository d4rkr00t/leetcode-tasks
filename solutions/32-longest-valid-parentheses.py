# Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
# hard
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def longestValidParentheses(s: str) -> int:
    dp = [0] * (len(s) + 1)
    ans = 0

    for i, ch in enumerate(s):
        j = i + 1

        if ch == "(" or i == 0:
            continue

        prevIdx = i - (dp[i] * 2) - 1
        if prevIdx >= 0 and s[prevIdx] == "(":
            if prevIdx - 1 >= 0 and s[prevIdx - 1] == ")":
                dp[j] = dp[i] + dp[prevIdx] + 1
            else:
                dp[j] = dp[i] + 1

        ans = max(ans, dp[j])

    print(dp)

    return ans * 2


print(longestValidParentheses("(()"), 2)
print(longestValidParentheses(")()())"), 4)
print(longestValidParentheses(")(())())(()"), 6)
print(longestValidParentheses("()(())"), 6)

#       prevIdx = 5 - (1 * 2) - 1 = 2
#       |
# _ ( ) ( ( ) )
#             |
#             ch
#
#           i = 5
#           |
# 0 0 1 0 0 1 0
#             |
#             j = 6
