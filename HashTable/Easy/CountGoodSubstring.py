# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        temp = 0
        for i in range(len(s)-2):
            x = s[i:i+3]
            if len(x) == len(set(x)):
                temp += 1
        return temp


obj = Solution()
res = obj.countGoodSubstrings("xyzzaz")
print(res)
