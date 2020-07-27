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
    def type(s):
        res = []
        for c in s:
            if c == "#":
                if res:
                    res.pop()
            else:
                res.append(c)

        return "".join(res)

    return type(S) == type(T)


print(backspaceCompare(S="ab#c", T="ad#c"), True)
print(backspaceCompare(S="ab##", T="c#d#"), True)
print(backspaceCompare(S="a##c", T="#a#c"), True)
print(backspaceCompare(S="a#c", T="b"), False)
