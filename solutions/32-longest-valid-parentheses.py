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
    dp = [0] * len(s)
    ans = 0

    for i in range(1, len(s)):
        if s[i-1] == "(" and s[i] == ")":
            dp[i] = dp[i-2] + 2 if i - 2 >= 0 else 2

        elif s[i-1] == ")" and s[i] == ")":
            idx = i - dp[i-1] - 1
            if idx >= 0 and s[idx] == "(":
                dp[i] = dp[i-1] + dp[idx-1] + 2

        ans = max(ans, dp[i])

    return ans


print(longestValidParentheses("(()"), 2)
print(longestValidParentheses(")()())"), 4)
print(longestValidParentheses(")(()())"), 6)
