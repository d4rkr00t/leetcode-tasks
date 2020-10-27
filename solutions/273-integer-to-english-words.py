# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# hard
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Recursion

def numberToWords(num: int) -> str:
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
        15: "Fifteen",
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
        10**2: "Hundred",
        10**3: "Thousand",
        10**6: "Million",
        10**9: "Billion"
    }

    def process(num):
        if num in table:
            return table[num]

        tens, ones = divmod(num, 10)
        return " ".join([table[tens * 10], table[ones]])

    ans = []

    for n in [10**9, 10**6, 10**3, 10**2]:
        nn, num = divmod(num, n)
        if nn:
            temp = numberToWords(nn)
            ans.append(" ".join([temp, table[n]]))

    if num:
        ans.append(process(num))

    return " ".join(ans)


print(numberToWords(123), "| One Hundred Twenty Three")
print(numberToWords(12345), "| Twelve Thousand Three Hundred Forty Five")
print(numberToWords(1234567),
      "| One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print(numberToWords(1234567891),
      "| One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
