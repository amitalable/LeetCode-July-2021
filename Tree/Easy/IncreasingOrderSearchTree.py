# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.arr = []

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        # self.inorder(root) will return a generator
        ans = cur = TreeNode(None)
        for v in self.inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

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


null = None
root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
obj = Solution()
root1 = obj.insert(root)
obj.increasingBST(root1)
