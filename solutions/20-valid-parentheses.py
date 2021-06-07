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
# TBD


def isValid(s: str) -> bool:
    stack = []
    pair = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in {"(", "[", "{"}:
            stack.append(ch)
        else:
            if not stack or stack.pop() != pair[ch]:
                return False

    return not stack


print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
