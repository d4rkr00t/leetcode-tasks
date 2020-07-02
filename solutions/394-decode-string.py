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
    cur_str = ""
    cur_num = 0
    for i, c in enumerate(s):
        if c == "[":
            stack.append(cur_str)
            stack.append(cur_num)
            cur_str = ""
            cur_num = 0
            continue

        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        elif c != "]":
            cur_str += c

        elif c == "]" or i == len(s) - 1:
            p_num = stack.pop()
            p_str = stack.pop()

            cur_str = p_str + cur_str * p_num

    return cur_str

print(decodeString("3[a]2[bc]"), "aaabcbc")
print(decodeString("3[a2[c]]"), "accaccacc")
print(decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
print(decodeString("100[leetcode]"))
