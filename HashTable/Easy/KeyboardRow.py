# https://leetcode.com/problems/keyboard-row/
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        res = []
        for w in words:
            w1 = w.lower()
            w1 = set(w1)
            if w1 <= s1 or w1 <= s2 or w1 <= s3:
                res.append(w)
        return res


obj = Solution()
print(obj.findWords(['ol']))
