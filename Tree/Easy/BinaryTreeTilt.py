# https://leetcode.com/problems/binary-tree-tilt/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            lv, rv = helper(root.left), helper(root.right)
            self.ans += abs(lv - rv)
            return root.val + lv + rv

        self.ans = 0
        helper(root)
        return self.ans
