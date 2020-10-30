# Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(n^2)
# Space: O(n+m)

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    def sum(n1, n2):
        ans = []
        p1 = len(n1) - 1
        p2 = len(n2) - 1
        carry = 0

        while p1 >= 0 or p2 >= 0:
            c1 = int(n1[p1]) if p1 >= 0 else 0
            c2 = int(n2[p2]) if p2 >= 0 else 0
            carry, n = divmod(c1+c2+carry, 10)
            ans.append(str(n))
            p1 -= 1
            p2 -= 1

        return "".join(ans[::-1])

    temp = [0] * (len(num1) + len(num2) - 1)

    for i, c1 in enumerate(num1[::-1]):
        n1 = int(c1)
        for j, c2 in enumerate(num2[::-1]):
            n2 = int(c2)
            temp[i+j] += n1 * n2

    ans = "0"
    for i, num in enumerate(temp):
        num = str(num) + ("0" * i)
        ans = sum(ans, num)

    return ans


print(multiply("2", "3"), "6")
print(multiply("123", "456"), "56088")
print(multiply("0", "0"), "0")
