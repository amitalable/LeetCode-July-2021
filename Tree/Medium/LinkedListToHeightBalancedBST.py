# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return self.sortedArrayToBST(l)
