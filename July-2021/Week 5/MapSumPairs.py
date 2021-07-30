# https://leetcode.com/problems/map-sum-pairs/


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}

    def insert(self, key: str, val: int) -> None:
        self.hashTable[key] = val

    def sum(self, prefix: str) -> int:
        prefix_len = len(prefix)
        res = 0
        for key, val in self.hashTable.items():
            if key[:prefix_len] == prefix:
                res += self.hashTable[key]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
