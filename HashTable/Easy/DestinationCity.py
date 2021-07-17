# https://leetcode.com/problems/destination-city/

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict(paths)
        for i in d.values():
            if i not in d.keys():
                return i
