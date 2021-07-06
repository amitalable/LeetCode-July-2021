# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            mid = len(nums)//2
            root = TreeNode(nums.pop(mid))
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid:])
            return root

    def levelOrderTraversal(self, root):
        stack = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                stack.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        return stack


obj = Solution()
nums = [-10, -3, 0, 5, 9]
root = obj.sortedArrayToBST(nums)
print(obj.levelOrderTraversal(root))
