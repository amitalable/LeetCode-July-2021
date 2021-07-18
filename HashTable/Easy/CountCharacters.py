# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/


from typing import Counter, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashTable = Counter(chars)
        res = 0
        for word in words:
            for ch in word:
                if hashTable[ch] < word.count(ch):
                    break
            else:
                res += len(word)
        return res
