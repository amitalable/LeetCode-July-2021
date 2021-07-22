# https://leetcode.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashTable = {}
        for v in nums2:
            while stack and stack[-1] < v:
                k = stack.pop()
                hashTable[k] = v
            stack.append(v)
        return [hashTable.get(v, -1) for v in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
