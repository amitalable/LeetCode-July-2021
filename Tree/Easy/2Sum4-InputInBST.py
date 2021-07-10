# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        res = []
        while stack:
            curr = stack.pop(0)
            if curr:
                if curr.val in res:
                    return True
                res.append(k - curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        return False
