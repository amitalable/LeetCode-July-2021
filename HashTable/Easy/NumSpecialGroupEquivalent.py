from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        d = {}
        for word in words:
            odd = []
            even = []
            for i, letter in enumerate(word):
                if i % 2 == 0:
                    even.append(letter)
                else:
                    odd.append(letter)
            odd = tuple(sorted(odd))
            even = tuple(sorted(even))
            x = tuple([odd, even])
            d[x] = d.get(x, 0)+1
        return len(d)

    def numSpecialEquivGroupsListComprehension(self, words: List[str]) -> int:
        return len(set(["".join(sorted(word[::2]))+"".join(sorted(word[1::2])) for word in words]))


print(Solution().numSpecialEquivGroupsListComprehension(
    ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))
