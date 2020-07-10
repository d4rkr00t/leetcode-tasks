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
    m = max(len(a), len(b))
    a = a.rjust(m, "0")
    b = b.rjust(m, "0")
    pos = m - 1
    carry = 0
    ans = ""

    while pos >= 0:
        if a[pos] == "1":
            carry += 1
        if b[pos] == "1":
            carry += 1

        if carry % 2 == 1:
            ans += "1"
        else:
            ans += "0"

        carry = carry // 2
        pos -= 1

    if carry == 1:
        ans += "1"

    return ans[::-1]


print(addBinary(a="11", b="1"), "100")
print(addBinary(a="1010", b="1011"), "10101")
