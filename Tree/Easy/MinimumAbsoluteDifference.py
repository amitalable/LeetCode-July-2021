# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = []

        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                l.append(root.val)

                if root.right:
                    inorder(root.right)

        inorder(root)
        return min(b-a for a, b in zip(l, l[1:]))
