# https://leetcode.com/problems/decode-ways-ii/
class Solution:
    def numDecodings(self, S):
        mod = 10**9 + 7
        a, b, c = 1, 0, 0
        for ch in S:
            if ch == '*':
                a, b, c = a*9+b*9+c*6, a, a
            else:
                a, b, c = (ch > '0') * a + b + (ch <= '6') * \
                    c, (ch == '1') * a, (ch == '2')*a

            a %= mod

        return a


print(Solution().numDecodings('10*'))
