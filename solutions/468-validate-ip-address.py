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
    def isValidIPv4(ip):
        segments = ip.split(".")
        if len(segments) < 4 or len(segments) > 4:
            return False

        for s in segments:
            if not s.isdigit():
                return False

            sint = int(s)
            if str(sint) != s:
                return False
            if sint < 0 or sint > 255:
                return False

        return "IPv4"

    def isValidIPv6(ip):
        segments = ip.split(":")
        chars = set("abcdefABCDEF0123456789")

        if len(segments) < 8 or len(segments) > 8:
            return False

        for s in segments:
            if len(s) < 1 or len(s) > 4:
                return False

            for ch in s:
                if ch not in chars:
                    return False

        return "IPv6"

    return isValidIPv4(IP) or isValidIPv6(IP) or "Neither"


print(validIPAddress("172.16.254.1"), "IPv4")
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
print(validIPAddress("256.256.256.256"), "Neither")
print(validIPAddress("172.16.@254.01"), "Neither")
