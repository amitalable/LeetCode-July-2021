# https://leetcode.com/problems/balanced-binary-tree/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0

    def isBalanced(self, root: TreeNode) -> bool:
        if root:
            if not self.isBalanced(root.left):
                return False
            if not self.isBalanced(root.right):
                return False
            if(abs(self.maxDepth(root.left)-self.maxDepth(root.right)) > 1):
                return False
            else:
                return True

        return True

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
arr = [1, 2, 2, 3, 3, null, null, 4, 4]
obj = Solution()
root = obj.insert(arr)
print(obj.isBalanced(root))
