# Guess the Word
# https://leetcode.com/problems/guess-the-word/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import defaultdict
from typing import List


def findSecretWord(wordlist: List[str], master) -> None:
    pass


# secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
# a c ck zz
# e i ow{zz} -> 2
# c{c}ba{zz} -> 3
# a{c}ck{zz} -> DONE!
