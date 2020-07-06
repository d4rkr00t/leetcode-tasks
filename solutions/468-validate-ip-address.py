# Validate IP Address
# https://leetcode.com/problems/validate-ip-address/
# medium
#
# Tags: Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def validIPAddress(IP: str) -> str:
    def validateV4(ip):
        if len(ip) != 4:
            return False

        for s in ip:
            if not s:
                return False

            if not s.isdigit():
                return False

            num = int(s)
            if num > 255 or num < 0 or str(num) != s:
                return False

        return True

    def validateV6(ip):
        if len(ip) != 8:
            return False

        for s in ip:
            if not s:
                return False

            if len(s) > 4:
                return False

            if not all(c in '0123456789abcdefABCDEF' for c in s):
                return False

        return True

    if ":" in IP and validateV6(IP.split(":")):
        return "IPv6"
    elif "." in IP and validateV4(IP.split(".")):
        return "IPv4"

    return "Neither"


print(validIPAddress("172.16..1"), "Neither")
print(validIPAddress("172.16.254.1"), "IPv4")
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
print(validIPAddress("256.256.256.256"), "Neither")
