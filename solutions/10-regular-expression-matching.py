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

# def isMatch(s: str, p: str) -> bool:
#     if not s and not p:
#         return True

#     if s and not p:
#         return False

#     isFirstMatch = p[0] in (s[0], ".") if s else False
#     isWildCard = p[1] == "*" if len(p) > 1 else False

#     if isWildCard:
#         return isMatch(s, p[2:]) or (isFirstMatch and isMatch(s[1:], p))

#     return isFirstMatch and isMatch(s[1:], p[1:])


def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[i, j]

        if j == len(p):
            memo[i, j] = i == len(s)
            return memo[i, j]

        isFirstMatch = p[j] in (s[i], ".") if i < len(s) else False
        isWildCard = p[j + 1] == "*" if j + 1 < len(p) else False
        ans = False

        if isWildCard:
            ans = dp(i, j + 2) or (isFirstMatch and dp(i + 1, j))
        else:
            ans = isFirstMatch and dp(i + 1, j + 1)

        memo[i, j] = ans
        return ans

    return dp(0, 0)


print(isMatch("aa", "a"), False)
print(isMatch("aa", "a*"), True)
print(isMatch("ab", ".*"), True)
print(isMatch("aab", "c*a*b"), True)
print(isMatch("mississippi", "mis*is*p*."), False)
print(isMatch("mississippi", "mis*is*ip*."), True)
