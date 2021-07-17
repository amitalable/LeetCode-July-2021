# https://leetcode.com/problems/sum-of-unique-elements/

from typing import Counter, List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashTable = Counter(nums)
        x = 0
        for num in hashTable.keys():
            if hashTable[num] == 1:
                x += num
        return x
