# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepthUsingRecursion(self, root: TreeNode) -> int:
        if root:
            if not root.left:
                return self.minDepth(root.right)+1
            elif not root.right:
                return self.minDepth(root.left)+1
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        return 0

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deque, depth = [root], 0
        while deque:
            levelsize = len(deque)
            depth += 1
            for _ in range(levelsize):
                t = deque.pop(0)
                if not t.left and not t.right:
                    return depth
                if t.left:
                    deque.append(t.left)
                if t.right:
                    deque.append(t.right)

        return depth
