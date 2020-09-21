# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isValid(s: str) -> bool:
    stack = []
    pairs = {"{": "}", "(": ")", "[": "]"}

    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
            continue

        if not stack:
            return False

        prev = stack.pop()
        if pairs[prev] != c:
            return False

    if stack:
        return False

    return True


print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
