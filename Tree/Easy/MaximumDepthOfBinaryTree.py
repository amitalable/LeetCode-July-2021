from math import log, ceil
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthUsingRecursion(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0

    def maxDepth(self, root: TreeNode) -> int:
        height = 0
        if not root:
            return 0

        q = [root]
        while q:
            height += 1
            temp = []
            for i in q:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            q = temp
        return height

    def insert(self, l: List[int]) -> TreeNode:
        root = None
        if l:
            root = TreeNode(l.pop(0))
            stack = [root]
            while l:
                # if there is only left node in l
                y = stack.pop(0)
                if y:
                    left = l.pop(0)
                    y.left = TreeNode(left) if left else None
                    if len(l) > 0:
                        right = l.pop(0)
                        y.right = TreeNode(right) if right else None
                        stack.append(y.left)
                        stack.append(y.right)
        return root


# [1, None, 2]  # [3, 9, 20, None, None, 15, 7]
root = [1, 2, None, 3, None, 4, None, 5]
obj = Solution()
root1 = obj.insert(root)
print(obj.maxDepth(root1))
