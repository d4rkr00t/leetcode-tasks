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
    table = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch not in table:
            stack.append(ch)
            continue

        if not stack:
            return False

        prev = stack.pop()
        if prev != table[ch]:
            return False

    return len(stack) == 0


print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
