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
    m = len(num1)
    n = len(num2)
    pos = [0] * (n + m)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1 = i + j
            p2 = i + j + 1
            sum = mul + pos[p2]

            pos[p1] += sum // 10
            pos[p2] = sum % 10

    while pos and   pos[0] == 0:
        pos.pop(0)

    return "".join([str(s) for s in pos]) if pos else "0"


print(multiply("2", "3"), "6")
print(multiply("123", "456"), "56088")
print(multiply("0", "0"), "0")

# 456
# 123

#  456
#  3
#   18
#  150
# 1200
# 1368
