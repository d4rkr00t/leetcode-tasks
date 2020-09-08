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
    def ipv4(ip):
        ss = ip.split(".")

        # x.x.x.x
        if len(ss) != 4:
            return False

        for s in ss:
            # x..x.x
            if not s or not s.isdigit():
                return False

            ns = int(s)

            # 192.01.1.1
            if str(ns) != s:
                return False

            if ns > 255 or ns < 0:
                return False

        return True

    def ipv6(ip):
        ss = ip.split(":")

        # x1:x2:x3:x4:x5:x6:x7:x8
        if len(ss) != 8:
            return False

        for s in ss:
            if len(s) < 1 or len(s) > 4:
                return False

            for c in s:
                if c not in "abcdefABCDEF0123456789":
                    return False

        return True

    if ipv4(IP):
        return "IPv4"

    if ipv6(IP):
        return "IPv6"

    return "Neither"


print(validIPAddress("172.16.254.1"), "IPv4")
print(validIPAddress("172.16.254.01"), "Neither")
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
print(validIPAddress("256.256.256.256"), "Neither")
