# Add Binary
# https://leetcode.com/problems/add-binary/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def addBinary(a: str, b: str) -> str:
    ans = ""
    a = list(a)
    b = list(b)
    carry = 0
    while a or b:
        c_a = int(a.pop()) if a else 0
        c_b = int(b.pop()) if b else 0

        s = c_a + c_b + carry

        if s % 2 == 1:
            ans = "1" + ans
        else:
            ans = "0" + ans

        carry = s // 2

    if carry:
        ans = "1" + ans

    return ans


print(addBinary(a="11", b="1"), "100")
print(addBinary(a="1010", b="1011"), "10101")
