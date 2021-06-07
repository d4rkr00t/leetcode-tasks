# Add Binary
# https://leetcode.com/problems/add-binary/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD


def addBinary(a: str, b: str) -> str:
    ans = []
    a = list(a)
    b = list(b)
    carry = 0

    while a or b:
        n1 = int(a.pop()) if a else 0
        n2 = int(b.pop()) if b else 0
        n = n1 + n2 + carry

        ans.append(str(n % 2))
        if n > 1:
            carry = 1
        else:
            carry = 0

    if carry:
        ans.append(str(carry))

    return "".join(ans[::-1])


print(addBinary(a="11", b="1"), "100")
print(addBinary(a="1010", b="1011"), "10101")
