# https://leetcode.com/problems/rotated-digits/

import re


class Solution:
    def rotatedDigits(self, n: int) -> int:

        x = list(map(str, range(1, n+1)))
        s = 0
        for i in x:
            if not re.search("[347]+", i) and re.search("[2569]+", i):
                s += 1

        return s


obj = Solution()
print(obj.rotatedDigits(10))
