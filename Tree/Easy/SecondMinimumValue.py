# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        arr = set()
        m = 2**31
        stack = [root]
        while stack:
            curr = stack.pop(0)
            if curr:
                arr.add(curr.val)
                m = min(m, curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        c = list(filter(lambda x: x != m, arr))
        return min(c, default=-1)
