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
    ans = [0] * len(num1)

    for p1 in range(len(num1)):
        n1 = int(num1[p1]) * pow(10, len(num1)-p1-1)
        for p2 in range(len(num2)):
            n2 = int(num2[p2]) * pow(10, len(num2)-p2-1)
            ans[p1] += n2 * n1

    return sum(ans)


print(multiply("2", "3"), "6")
print(multiply("123", "456"), "56088")
print(multiply("0", "0"), "0")
