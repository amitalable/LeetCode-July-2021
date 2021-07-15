# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

from typing import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter(sentence)) == 26


print(Solution().checkIfPangram("abc"))
