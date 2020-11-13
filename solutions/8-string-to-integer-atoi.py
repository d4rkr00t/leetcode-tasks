# String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# medium
#
# Tags: Facebook, Microsoft
#
# Time:  O(n)
# Space: O(1)

def myAtoi(s: str) -> int:
    ans = sign = 0
    max_int = 2**31

    for ch in s:
        if ch == " " and not ans and not sign:
            continue

        if ans >= max_int:
            break
        elif ch.isdigit():
            if not sign:
                sign = 1
            ans = ans * 10 + int(ch)
        elif (ch == "+" or ch == "-") and not sign:
            sign = 1 if ch != "-" else -1
        else:
            break

    ans = ans * sign

    if ans < 0:
        return ans if ans >= -max_int else -max_int


print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)
