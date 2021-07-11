# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.l = []

        def inorder(root):
            if root:
                inorder(root.left)
                self.l.append(root.val)
                inorder(root.right)
        inorder(root)
        m = 10**5+1
        for i in range(1, len(self.l)):
            m = min(m, self.l[i] - self.l[i-1])
        return m
