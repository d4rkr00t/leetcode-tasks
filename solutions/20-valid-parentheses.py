# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)


def isValid(s: str) -> bool:
    stack = []
    oc_map = {"}": "{", ")": "(", "]": "["}

    for ch in s:
        if ch in oc_map:
            if not stack or stack[-1] != oc_map[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


print(isValid("()"), True)
print(isValid("()[]{}"), True)
print(isValid("(]"), False)
print(isValid("([)]"), False)
print(isValid("{[]}"), True)
