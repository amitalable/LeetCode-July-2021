# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphicUsing2Dic(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False
        x = y = 0
        s_str = t_str = ''
        s_dic, t_dic = {}, {}
        for i in range(s_len):
            if (s[i] in s_dic.keys() and not t[i] in t_dic.keys())\
                    or (not s[i] in s_dic.keys() and t[i] in t_dic.keys()):
                return False
            if not (s[i] in s_dic.keys() and t[i] in t_dic.keys()):
                s_dic[s[i]] = x
                t_dic[t[i]] = y
            s_str += str(s_dic[s[i]])
            t_str += str(t_dic[t[i]])
            x += 1
            y += 1
        return s_str == t_str

    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        common_dic = {}
        for i in range(len(s)):
            if s[i] in common_dic:
                if common_dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in common_dic.values():
                    return False
                else:
                    common_dic[s[i]] = t[i]
        return True


obj = Solution()
print(obj.isIsomorphic("paper", "title"))
