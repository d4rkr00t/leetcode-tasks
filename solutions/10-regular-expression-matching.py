# Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[i, j]

        if j == len(p):
            ans = i == len(s)
        else:
            first_match = i < len(s) and p[j] in {s[i], "."}
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                ans = first_match and dp(i + 1, j + 1)

        memo[i, j] = ans
        return ans

    return dp(0, 0)


print(isMatch("a", "a*"), True)
print(isMatch("ab", "a*"), False)
print(isMatch("a", "a"), True)
print(isMatch("aa", "a"), False)
print(isMatch("aa", "a*"), True)
print(isMatch("ab", ".*"), True)
print(isMatch("aab", "c*a*b"), True)
print(isMatch("mississippi", "mis*is*p*."), False)
