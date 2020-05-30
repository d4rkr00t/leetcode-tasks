# Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
# easy
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  O(S+T)
# Space: O(max(S,T))
#
# Solution:
# Two stacks

def backspaceCompare(S: str, T: str) -> bool:
    def process(s):
        stack = []
        for c in s:
            if c == "#" and stack: stack.pop()
            elif c != "#": stack.append(c)

        return "".join(stack)

    return process(S) == process(T)

print(backspaceCompare(S = "ab#c", T = "ad#c"), True)
print(backspaceCompare(S = "ab##", T = "c#d#"), True)
print(backspaceCompare(S = "a##c", T = "#a#c"), True)
print(backspaceCompare(S = "a#c", T = "b"), False)
