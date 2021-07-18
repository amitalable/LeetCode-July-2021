# https://leetcode.com/problems/relative-sort-array/

from typing import Counter, List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashTable = Counter(arr1)
        temp = []
        for num in arr2:
            temp += [num]*hashTable[num]
            del hashTable[num]
        x = []
        for k, v in hashTable.items():
            x += [k]*v
        return temp + sorted(x)
