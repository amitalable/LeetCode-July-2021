# https://leetcode.com/problems/univalued-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        s = root.val
        while stack:
            curr = stack.pop(0)
            if s != curr.val:
                return False
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return True
