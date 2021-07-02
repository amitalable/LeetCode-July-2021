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

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        return self.inOrder(root, [])
