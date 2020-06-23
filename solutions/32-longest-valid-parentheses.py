# Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
# hard
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def longestValidParentheses(s: str) -> int:
    dp = [0] * len(s)
    ans = 0

    for i in range(1, len(s)):
        if s[i] == ")" and s[i-1] == "(":
            dp[i] = (0 if i-2 < 0 else dp[i-2]) + 2

        if s[i] == ")" and i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
            dp[i] = dp[i-1] + (0 if i - dp[i-1] < 2 else dp[i - dp[i-1] - 2]) + 2

        ans = max(ans, dp[i])

    return ans



print(longestValidParentheses("(()"), 2)
print(longestValidParentheses("((())("), 4)
print(longestValidParentheses(")()())"), 4)

