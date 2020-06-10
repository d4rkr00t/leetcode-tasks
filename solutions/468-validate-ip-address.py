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
    def is_valid_v4(IP: str):
        if IP.find(".") == -1: return False

        segments = IP.split(".")

        if len(segments) != 4:
            return False

        for s in segments:
            # 127..1.0
            if len(s) == 0:
                return False

            if s[0] == "-":
                return False

            # 256.1.0.1
            try:
                num = int(s)
                if num > 255 or str(num) != s:
                    return False
            except:
                return False

        return True

    def is_valid_v6(IP: str):
        if IP.find(":") == -1: return False

        segments = IP.split(":")

        # 2001:0db8:85a3:8A2E:0370:7334
        if len(segments) != 8:
            return False

        for s in segments:
            # 2001:0db8:85a3::8A2E:0370:7334
            if len(s) == 0:
                return False

            # 256.1.0.1
            if len(s) > 4:
                return False

            try:
                num = int(s, 16)
            expect:
                return False

        return True

    if is_valid_v4(IP):
        return "IPv4"

    if is_valid_v6(IP):
        return "IPv6"

    return "Neither"

print(validIPAddress("172.16.254.1"), "IPv4")
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
print(validIPAddress("2001:0db8:85a3::8A2E:0370:7334"), "Neither")
print(validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"), "Neither")
print(validIPAddress("256.256.256.256"), "Neither")
