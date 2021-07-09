# https://leetcode.com/problems/sum-of-left-leaves
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.x = 0

        def dfs(root):
            if not root:
                return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.x += root.left.val
                else:
                    dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.x
