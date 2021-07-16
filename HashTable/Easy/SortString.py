# https://leetcode.com/problems/increasing-decreasing-string

from typing import Counter


class Solution:
    def sortString(self, s: str) -> str:
        '''
            1. Pick the smallest character from s and append it to the result.
            2. Pick the smallest character from s which is greater than the last 
               appended character to the result and append it.
            3. Repeat step 2 until you cannot pick more characters.
            4. Pick the largest character from s and append it to the result.
            5. Pick the largest character from s which is smaller than the last 
               appended character to the result and append it.
            6. Repeat step 5 until you cannot pick more characters.
            7. Repeat the steps from 1 to 6 until you pick all characters from s
        '''
        hashTable = Counter(s)
        out = ""
        keys = list(sorted(hashTable.keys()))
        while hashTable:
            for key in keys:
                if key in hashTable:
                    hashTable[key] -= 1
                    out += key
                    if hashTable[key] < 1:
                        del hashTable[key]
            keys = keys[::-1]

        return out


s = "leetcode"   # Output "abccbaabccba"
obj = Solution()
print(obj.sortString(s))
