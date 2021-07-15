# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    break
            else:
                m += 1
        return m
