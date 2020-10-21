# Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
# hard
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)

def longestValidParentheses(s: str) -> int:
    dp = [0] * len(s)
    ans = 0

    for i in range(1, len(s)):
        if s[i] == ")":
            if s[i-1] == "(":
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2]
                                   if i-dp[i-1] >= 2 else 0) + 2

        ans = max(ans, dp[i])

    return ans


# print(longestValidParentheses("(()"), 2)
# print(longestValidParentheses(")()())"), 4)
# print(longestValidParentheses(")(()())"), 6)
print(longestValidParentheses("()(()"), 2)
print(longestValidParentheses("()(())"), 6)
