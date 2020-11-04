# Add Binary
# https://leetcode.com/problems/add-binary/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(max(n,m))
# Space: O(1)
#
# Solution:
# TBD

def addBinary(a: str, b: str) -> str:
    carry = 0
    ans = []
    a = list(a)
    b = list(b)

    while a or b:
        n = int(a.pop()) if a else 0
        m = int(b.pop()) if b else 0
        carry, t = divmod(n + m + carry, 2)
        ans.append(str(t))

    if carry:
        ans.append(str(carry))

    return "".join(reversed(ans))


print(addBinary(a="11", b="1"), "100")
print(addBinary(a="1010", b="1011"), "10101")
print(addBinary(a="1011", b="1011"), "10101")
