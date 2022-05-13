# Decode String
# https://leetcode.com/problems/decode-string/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def decodeString(s: str) -> str:
    stack = []
    digit = 0

    for ch in s:
        if ch.isdigit():
            digit = digit * 10 + int(ch)
            continue

        if digit:
            stack.append(digit)
            digit = 0

        if ch == "]":
            string = ""
            while stack[-1] != "[":
                string = stack.pop() + string

            stack.pop()
            reps = stack.pop()
            stack.append(string * reps)
        else:
            stack.append(ch)

    return "".join(stack)


print(decodeString("3[a]2[bc]"), "aaabcbc")
print(decodeString("3[a2[c]]"), "accaccacc")
print(decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
print(decodeString("100[leetcode]"))
