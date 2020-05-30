# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Stack

def isValid(s: str) -> bool:
    stack = []
    pairs = { "{": "}", "(": ")", "[": "]" }

    for c in s:
        if c in pairs:
            stack.append(c)
        elif stack:
            prev = stack.pop()
            if pairs[prev] != c:
                return False
        else:
            return False

    return True if not stack else False

print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
