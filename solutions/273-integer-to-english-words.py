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

    num_to_word = {
        10**9: "Billion",
        10**6: "Million",
        10**3: "Thousand",
        10**2: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }

    ans = []

    def encode(num):
        q, num = divmod(num, 10**2)
        res = []
        if q:
            res.append(encode(q))
            res.append("Hundred")

        q, num = divmod(num, 10)
        if q > 1:
            res.append(num_to_word[q*10])
            if num:
                res.append(num_to_word[num])
        elif q == 1:
            res.append(num_to_word[q*10+num])
        elif num:
            res.append(num_to_word[num])

        return " ".join(res)

    for p in [10**9, 10**6, 10**3]:
        word = num_to_word[p]
        q, num = divmod(num, p)
        if q:
            ans.append(encode(q))
            ans.append(word)

    if num:
        ans.append(encode(num))

    return " ".join(ans)


print(numberToWords(123), "| One Hundred Twenty Three")
print(numberToWords(12345), "| Twelve Thousand Three Hundred Forty Five")
print(numberToWords(1234567),
      "| One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print(numberToWords(1234567891),
      "| One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
