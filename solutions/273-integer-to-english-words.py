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
    if num == 0:
        return "Zero"

    table = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fiveteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Fourty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion",
    }

    def processSmallNum(num):
        res = []
        hundreds, num = divmod(num, 100)
        if hundreds:
            res.append(table[hundreds])
            res.append(table[100])

        if num > 19:
            tens, num = divmod(num, 10)
            res.append(table[tens * 10])

        res.append(table[num])

        return " ".join(res)

    res = []
    for nn in [10**9, 10**6, 10**3]:
        cur, num = divmod(num, nn)
        cur_name = table[nn]
        if cur:
            res.append(processSmallNum(cur))
            res.append(cur_name)

    if num:
        res.append(processSmallNum(num))

    return " ".join(res)


print(numberToWords(123), "| One Hundred Twenty Three")
print(numberToWords(12345), "| Twelve Thousand Three Hundred Forty Five")
print(
    numberToWords(1234567),
    "| One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print(
    numberToWords(1234567891),
    "| One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
)
