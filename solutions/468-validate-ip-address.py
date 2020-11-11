# Validate IP Address
# https://leetcode.com/problems/validate-ip-address/
# medium
#
# Tags: Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)

def validIPAddress(IP: str) -> str:
    def vaildateIPv4(IP):
        sections = IP.split('.')

        if len(sections) != 4:
            return False

        for s in sections:
            if not s or not s.isdigit():
                return False

            s_num = int(s)

            if s_num < 0 or s_num > 255:
                return False

            if str(s_num) != s:
                return False

        return True

    def vaildateIPv6(IP):
        sections = IP.split(':')
        chars = set("abcdefABCDEF0123456789")

        if len(sections) != 8:
            return False

        for s in sections:
            if not s or len(s) > 4:
                return False

            if not all([ch in chars for ch in s]):
                return False

        return True

    if vaildateIPv4(IP):
        return "IPv4"

    if vaildateIPv6(IP):
        return "IPv6"

    return "Neither"


print(validIPAddress("172.16.254.1"), "IPv4")
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
print(validIPAddress("256.256.256.256"), "Neither")
