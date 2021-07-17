# https://leetcode.com/problems/unique-number-of-occurrences

from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashTable = Counter(arr)
        return len(hashTable.values()) == len(set(hashTable.values()))


print(Solution().uniqueOccurrences([1, 2, 3]))
