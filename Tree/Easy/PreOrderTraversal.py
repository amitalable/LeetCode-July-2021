# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return[]
        stack = [root]
        preorder = []
        while stack:
            temp = stack.pop()
            preorder.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return preorder

    def preorderTraversalUsingRecursion(self, root: TreeNode) -> List[int]:
        def preOrder(root: TreeNode, preorder: List[int]):
            if root:
                preorder.append(root.val)
                if root.left:
                    preOrder(root.left, preorder)
                if root.right:
                    preOrder(root.right, preorder)
            return preorder

        return preOrder(root, [])
