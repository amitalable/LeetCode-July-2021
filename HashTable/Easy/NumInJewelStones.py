# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashTable = dict()
        for ch in jewels:
            hashTable[ch] = 0
        for ch in stones:
            if ch in hashTable.keys():
                hashTable[ch] += 1
        return sum(hashTable.values())
