# Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    ans = ""

    num1 = num1[::-1]
    num2 = num2[::-1]

    def plus(n1, n2):
        n1 = n1[::-1]
        n2 = n2[::-1]
        res = ""
        pos = 0
        carry = 0
        while len(n1) > pos or len(n2) > pos:
            n1n = int(n1[pos]) if pos < len(n1) else 0
            n2n = int(n2[pos]) if pos < len(n2) else 0
            carry, tmp = divmod(carry + n1n + n2n, 10)
            res = str(tmp) + res
            pos += 1

        if carry:
            res = str(carry) + res

        return res

    def mul(n1, n2, zeros=0):
        if n1 == "0" or n2 == "0":
            return "0"

        return str(int(n1) * int(n2)) + ("0" * zeros)

    for i in range(len(num1)):
        for j in range(len(num2)):
            ans = plus(mul(num1[i], num2[j], i + j), ans)

    return ans


print(multiply("2", "3"), "6")
print(multiply("123", "456"), "56088")
print(multiply("0", "0"), "0")

#     1 2 3
#     4 5 6
#
#     7 3 8
#   6 1 5 0
# 4 9 2 0 0
# 5 6 0 8 8
