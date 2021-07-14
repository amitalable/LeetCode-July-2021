from collections import Counter


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        '''
        1. Creates a HashTable for each character and add its occurences for str
        2. For every element in order add its number of occurences into ans
        3. Add the remaining elements of str in ans which are not present in order  
        '''

        hashTable = Counter(str)
        ans = ""
        for char in order:
            ans += char * hashTable[char]
            hashTable[char] = 0
        for char, occurence in hashTable.items():
            ans += char * occurence
        return ans


print(Solution().customSortString("cbafg", "abcd"))
