# Text Justification
# https://leetcode.com/problems/text-justification/
# hard
#
# Tags: Google, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import math
from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    ans = []
    c = 0
    line = []

    def formatLine(line, maxWidth):
        if len(line) == 1:
            res = line[0]
            return res + (" " * (maxWidth - len(res)))

        res = ""
        w = sum([len(w) for w in line])
        fill = maxWidth - w
        sp = len(line) - 1

        for i, word in enumerate(line):
            if i != 0:
                sw = math.ceil(fill / sp)
                res += " " * sw
                fill -= sw
                sp -= 1

            res += word

        return res

    for word in words:
        cc = c + len(word) + (0 if len(line) == 0 else 1)

        # End of a line
        if cc > maxWidth:
            ans.append(formatLine(line, maxWidth))
            line = [word]
            c = len(word)
        else:
            c = cc
            line.append(word)

    if line:
        tmp = " ".join(line)
        ans.append(tmp + (" " * (maxWidth - len(tmp))))

    return ans


print(
    fullJustify(words=[
        "Science", "is", "what", "we", "understand", "well", "enough", "to",
        "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
        "we", "do"
    ],
                maxWidth=20),
    [
        "Science  is  what we", "understand      well", "enough to explain to",
        "a  computer.  Art is", "everything  else  we", "do                  "
    ])

[
    'Science  is  what we', 'understand      well', 'enough to explain to',
    'a  computer.  Art is', 'everything  else  we', 'do                  '
]
[
    'Science  is  what we', 'understand      well', 'enough to explain to',
    'a  computer.  Art is', 'everything  else  we', 'do                  '
]

[
    "ask   not   what", "your country can", "do  for  you ask",
    "what  you  can do", "for your country"
]
[
    "ask   not   what", "your country can", "do  for  you ask",
    "what  you  can do", "for your country"
]
