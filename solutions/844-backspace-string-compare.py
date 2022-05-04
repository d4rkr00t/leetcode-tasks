# Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
# easy
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def backspaceCompare(S: str, T: str) -> bool:
    def simulate(s):
        stack = []
        for ch in s:
            if ch == "#":
                if stack: stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

    return simulate(S) == simulate(T)


print(backspaceCompare(S="ab#c", T="ad#c"), True)
print(backspaceCompare(S="ab##", T="c#d#"), True)
print(backspaceCompare(S="a##c", T="#a#c"), True)
print(backspaceCompare(S="a#c", T="b"), False)
