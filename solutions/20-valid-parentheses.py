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
    if not s: return True
    pairs = { ")": "(", "]": "[", "}": "{" }
    stack = []

    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
            continue

        o = pairs[c]

        if not stack or stack[-1] != o:
            return False

        stack.pop()


    if stack:
        return False

    return True



print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
