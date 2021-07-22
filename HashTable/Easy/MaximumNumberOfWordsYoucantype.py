# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split(" "):
            for ch in word:
                if ch in brokenLetters:
                    break

            else:
                res += 1
        return res
