# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# hard
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def numberToWords(num: int) -> str:
    num_str = str(num)
    sections = []
    for i in range(len(num_str)-1, -1, -3):
        sections.append(num_str[max(i-2, 0):i+1])

    sections.reverse()

    mappings = {
        3: "Billion",
        2: "Million",
        1: "Thousand",
        0: ""
    }

    num_mappings = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fivteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
        "20": "Twenty",
        "30": "Thirty",
        "40": "Fourty",
        "50": "Fifty",
        "60": "Sixty",
        "70": "Seventy",
        "80": "Eighty",
        "90": "Ninety",
    }

    def join_str(strs):
        return " ".join([s for s in strs if s])

    def process_section(section):
        nonlocal num_mappings
        if section[0] in num_mappings:
            return join_str([num_mappings[section[0]], section[1]])

        if len(section[0]) == 3:
            return join_str([process_section((section[0][:1], "Hundred")), process_section((section[0][1:], "")), section[1]])

        return join_str([num_mappings[section[0][0] + "0"],  num_mappings[section[0][1]], section[1]])

    for i,s in enumerate(sections):
        sections[i] = process_section((sections[i], mappings[len(sections) - i - 1]))

    print(sections)

    return " ".join(sections)

print(numberToWords(123), "One Hundred Twenty Three")
print(numberToWords(12345), "Twelve Thousand Three Hundred Forty Five")
print(numberToWords(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print(numberToWords(1234567891), "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
