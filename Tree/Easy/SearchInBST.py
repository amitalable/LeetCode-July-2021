# https://leetcode.com/problems/search-in-a-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
