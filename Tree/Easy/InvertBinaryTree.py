# https://leetcode.com/problems/invert-binary-tree
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        dq = [root]

        while dq:
            curr = dq.pop(0)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        return root
