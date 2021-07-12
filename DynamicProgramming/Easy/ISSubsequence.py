# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        s1 = 0
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i])+1:]
                s1 += 1
            else:
                return False
            if len(s) == s1:
                return True
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        left_bound = len(s)
        right_bound = len(t)
        p_left = p_right = 0
        while p_left < left_bound and p_right < right_bound:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == left_bound


obj = Solution()
print(obj.isSubsequence("abc", "ahbgdc"))
