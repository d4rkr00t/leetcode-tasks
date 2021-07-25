# Sum of Digits of String After Convert
# https://leetcode.com/contest/weekly-contest-251/problems/sum-of-digits-of-string-after-convert/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def getLucky(s: str, k: int) -> int:
    def transform(s):
        ans = 0

        for ch in s:
            ans += int(ch)

        return str(ans)

    cur = ""

    for ch in s:
        cur += str(ord(ch) - ord("a") + 1)

    for i in range(k):
        cur = transform(cur)

    return int(cur)


print(getLucky(s="iiii", k=1), 36)
print(getLucky(s="leetcode", k=2), 6)
print(getLucky(s="zbax", k=2), 8)
