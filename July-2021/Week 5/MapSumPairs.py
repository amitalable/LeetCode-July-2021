# https://leetcode.com/problems/map-sum-pairs/


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}

    def insert(self, key: str, val: int) -> None:
        self.hashTable[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.hashTable.items()
                   if key.startswith(prefix))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
