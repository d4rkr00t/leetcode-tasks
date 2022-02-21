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
    curNum = 0
    curStr = ""

    for ch in s:
        if ch == "[":
            stack.append(curNum)
            stack.append("[")
            curNum = 0
        elif ch.isdigit():
            if curStr:
                stack.append(curStr)
                curStr = ""
            curNum = curNum * 10 + int(ch)
        elif ch == "]":
            resStr = curStr
            curStr = ""
            while stack and stack[-1] != "[":
                resStr = stack.pop() + resStr

            if stack and stack[-1] == "[":
                stack.pop()
                n = stack.pop()
                resStr *= n

            stack.append(resStr)

        else:
            curStr += ch

    if curStr:
        stack.append(curStr)

    return "".join(stack)


print(decodeString("3[a]2[bc]"), "aaabcbc")
print(decodeString("3[a2[c]]"), "accaccacc")
print(decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
print(decodeString("leetcode"), "leetcode")
print(decodeString("a2[b]"), "abb")
print(decodeString("10[leetcode]"))

# "3[a2[c3[b]a]]ef3[a]bc"
#                      |
#  stack = ["acbbbacbbaacbbbacbbaacbbbacbba", "ef", "aaa", "bc"]
#  curNum = None
#  curStr = "bc"
#  resStr = ""
