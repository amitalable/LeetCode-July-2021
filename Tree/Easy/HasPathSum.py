# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def sol(root, su):
            if not root:
                return False
            su += root.val
            if not root.left and not root.right:
                return su == targetSum
            return sol(root.left, su) or sol(root.right, su)
        return sol(root, 0)
