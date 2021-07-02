# https://leetcode.com/problems/binary-tree-postorder-traversal

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return[]
        stack = [root]
        postorder = []
        while stack:
            temp = stack.pop()
            postorder.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return postorder[::-1]

    def postorderTraversalUsingRecursion(self, root: TreeNode) -> List[int]:
        def postOrder(root: TreeNode, postorder: List[int]):
            if root:
                postOrder.append(root.val)
                if root.left:
                    postOrder(root.left, postorder)
                if root.right:
                    postOrder(root.right, postorder)
            return postorder[::-1]

        return postOrder(root, [])
