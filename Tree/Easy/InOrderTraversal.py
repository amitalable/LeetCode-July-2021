# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, root, result):
        if not root:
            return
        if root.left:
            self.inOrder(root.left, result)
        result.append(root.val)
        if root.right:
            self.inOrder(root.right, result)

        return result

    def inorderTraversalUsingRecursion(self, root: TreeNode) -> List[int]:
        if not root:
            return
        return self.inOrder(root, [])

    def inorderTraversalUsingStack(self, root: TreeNode) -> List[int]:
        current = root
        stack, res = [], []  # initialize stack
        while True:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif(stack):
                current = stack.pop()
                res.append(current.val)
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break
        return res
